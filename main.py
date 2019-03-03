import os

from flask import Flask, render_template, request, session

import boto3

import json
import nanonets

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lol'

S3_URL = 'https://s3-us-west-2.amazonaws.com'
S3_BUCKET = 'passion-project-test'


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/upload', methods=['GET'])
def uploaded_view():
    image_url = session['image_url']

    classification = nanonets.send_image_to_api(image_url)

    print(classification)

    result = classification['result'][0]
    if result['message'] == 'Failure':
        classification['message'] = 'Failure'

    prediction = result['prediction'][0] if result['prediction'] else None

    return render_template('upload_success.html',
                           image_url=image_url,
                           classification=classification,
                           prediction=prediction)



@app.route('/sign_s3', methods=['GET'])
def sign_s3():
    file_name = request.args.get('file_name')
    file_type = request.args.get('file_type')

    s3 = boto3.client('s3')

    presigned_post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl": "public-read", "Content-Type": file_type},
        Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn = 3600
    )

    image_url = '{}/{}/{}'.format(S3_URL, S3_BUCKET, file_name)
    session['image_url'] = image_url

    return json.dumps({
        'data': presigned_post,
        'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
    })



if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
