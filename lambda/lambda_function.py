import boto3
from PIL import Image
import io
import os
from datetime import datetime

# AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def lambda_handler(event, context):
    # Get the bucket and object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Ignore already resized images
    if key.startswith("thumbnails/"):
        return
    
    # Download the image from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    img = Image.open(obj['Body'])

    # Resize image
    img.thumbnail((128, 128))
    buffer = io.BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)

    # Define thumbnail key
    thumb_key = f'thumbnails/{os.path.basename(key)}'

    # Upload resized image to thumbnails folder
    s3.put_object(
        Bucket=bucket,
        Key=thumb_key,
        Body=buffer,
        ContentType='image/jpeg'
    )

    # ✅ Store metadata in DynamoDB
    table.put_item(Item={
        'filename': os.path.basename(key),
        'original_key': key,
        'resized_key': thumb_key,
        'upload_time': datetime.utcnow().isoformat(),
        's3_url': f"https://{bucket}.s3.amazonaws.com/{thumb_key}"
    })

    return {
        'statusCode': 200,
        'body': f"Thumbnail created and metadata stored for {key}"
    }
