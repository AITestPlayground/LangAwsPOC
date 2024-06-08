import os
import boto3

class S3Uploader:
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_path, s3_key):
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(f"Uploaded {file_path} to s3://{self.bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Failed to upload {file_path} to S3: {str(e)}")

    def upload_directory(self, directory_path, s3_prefix=""):
        if not os.path.isdir(directory_path):
            print(f"Directory {directory_path} does not exist")
            return

        for root, _, files in os.walk(directory_path):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, directory_path)
                s3_key = os.path.join(s3_prefix, relative_path)
                
                # Standardize s3_key to use '/' as a separator, which is required by S3
                s3_key = s3_key.replace(os.sep, '/')
                self.upload_file(local_path, s3_key)

# Example usage
# uploader = S3Uploader(bucket_name="mybucketprefix-dc6ce169-9870-411a-a6b7-d79cd1ceb391")
# uploader.upload_directory("documents","documents/")  
