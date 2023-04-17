import boto3


s3 = boto3.client('s3')

file = "<csvFile>"
bucket = "<bucketName>"

s3.upload_file(file, bucket, file)