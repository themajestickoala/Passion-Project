from flask import Flask, render_template, request, session

import s3
import nanonets

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lol'

S3_URL = 'https://s3-us-west-2.amazonaws.com'
S3_BUCKET_NAME = 'passion-project-test'
S3_FOLDER = 'images'


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files.get('file')
    s3.upload_file(S3_BUCKET_NAME, S3_FOLDER, image)

    image_url = '{}/{}/{}/{}'.format(S3_URL, S3_BUCKET_NAME, S3_FOLDER, image.filename)

    session['image_url'] = image_url

    classification = nanonets.send_image_to_api(image_url)

    print(classification)

    result = classification['result'][0]
    prediction = result['prediction'][0]

    return render_template('upload_success.html',
                           image_url=image_url,
                           classification=classification,
                           prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
