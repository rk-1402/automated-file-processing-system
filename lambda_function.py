import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Read file
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Process content
        processed_content = content.upper()

        # Save output
        output_bucket = "my-s3-project-output"
        output_key = "processed-" + key

        s3.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=processed_content
        )

    return "Processing complete"
