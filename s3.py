import boto3

S3 = boto3.resource('s3')

def upload_file(bucket_name, path, data_file):
    file_contents = data_file.read()

    s3_object = S3.Object(bucket_name, '{}/{}'.format(path, data_file.filename))
    s3_object.put(Body=file_contents)
