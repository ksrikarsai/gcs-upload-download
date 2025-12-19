import os
import pathlib
import mimetypes
from google.cloud import storage
STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')

class GCStorage:
    def __init__(self,storage_client):
        self.client = storage_client   
    
    def create_bucket(self, bucket_name, storage_class, bucket_location='US'):
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = storage_class
        return self.client.create_bucket(bucket, bucket_location) 
       
    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)   
     
    def list_buckets(self):
        buckets = self.client.list_buckets()
        return [bucket.name for bucket in buckets]    
    
    def upload_file(self, bucket, blob_destination, file_path):
        file_type = file_path.split('.')[-1]
        if file_type == 'csv':
            content_type = 'text/csv'
        elif file_type == 'psd':
            content_type = 'image/vnd.adobe.photoshop'
        else:
            content_type = mimetypes.guess_type(file_path)[0]
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(file_path, content_type=content_type)
        return blob
    
    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)
    
#Prepare variables
working_dir = pathlib.Path.cwd()
files_folder = working_dir.joinpath('My Files')
downloads_folder = working_dir.joinpath('Downloaded')
bucket_name = 'gcs_api_demo1'

files_folder.mkdir(exist_ok=True)
downloads_folder.mkdir(exist_ok=True)

#Construct GCStorage instance
storage_client = storage.Client()
gcs = GCStorage(storage_client)

#Create gcp_api_demo Cloud Storage Bucket
if bucket_name not in gcs.list_buckets():
    buckets_gcs = gcs.create_bucket(bucket_name, STORAGE_CLASSES[0])
else:
    bucket_gcs = gcs.get_bucket(bucket_name)

#Upload Files
for file_path in files_folder.glob('*.*'):
    #Use file name without extension
    gcs.upload_file(bucket_gcs, 'without extension/' + file_path.stem, str(file_path))
    #Use full file name
    gcs.upload_file(bucket_gcs, file_path.name, str(file_path))

#Download Files
gcs_demo_blobs = gcs.list_blobs('gcs_api_demo1')
for blob in gcs_demo_blobs:
    path_download = downloads_folder.joinpath(blob.name)
    if not path_download.parent.exists():
        path_download.parent.mkdir(parents=True)
    blob.download_to_filename(str(path_download))


