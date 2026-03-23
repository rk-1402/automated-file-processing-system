import boto3

s3 = boto3.client('s3')

bucket = "my-s3-project-input"
file_name = "test.txt"

with open(file_name, "w") as f:
    f.write("hello from ec2")

s3.upload_file(file_name, bucket, file_name)

print("File uploaded successfully!")
