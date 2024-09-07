
from celery import shared_task
import boto3
from django.conf import settings
import os


@shared_task(queue='images_queue')
def upload_image_to_s3(file_path, s3_path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )
    
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    try:
        with open(file_path, 'rb') as file:
            s3.upload_fileobj(file, bucket_name, s3_path)
        
        os.remove(file_path)
    except Exception as e:
        print(f"Error al subir la imagen a S3: {e}")
        return False
    return True
