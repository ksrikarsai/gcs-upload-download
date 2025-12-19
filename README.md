# Google Cloud Storage File Upload & Download (Python)

This project demonstrates how to upload and download files using the Google Cloud Storage API with Python.

## Features
- Upload local files to Google Cloud Storage
- Download files from Google Cloud Storage
- Automatically creates required local folders
- Preserves folder structure during download
- Uses Google Cloud Application Default Credentials (ADC)

## Folder Structure
- Uploaded/ → Place files here to upload to cloud
- My Files/ → Files downloaded from cloud

## Prerequisites
- Python 3.x
- Google Cloud account
- Google Cloud CLI installed
- Cloud Storage API enabled

## Setup Instructions

```bash
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/gcs-upload-download.git
cd gcs-upload-download

2. Install dependencies
pip install -r requirements.txt

3. Authenticate with Google Cloud
gcloud auth application-default login

4. Run the script
python uploaddownload.py
```


## Notes

- Bucket name must be globally unique

- Files placed in the Uploaded folder will be uploaded to Google Cloud Storage

- Downloaded files will appear in the My Files folder

- No credentials or secrets are stored in the repository

## Technologies Used

- Python

- Google Cloud Storage


