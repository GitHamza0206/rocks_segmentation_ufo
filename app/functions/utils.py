# import the necessary packages
from google.oauth2 import service_account
from googleapiclient.discovery import build # type: ignore
from googleapiclient.http import MediaIoBaseDownload # type: ignore
import os

def grab_images_from_drive():
    # Set up Google Drive API credentials
    credentials = service_account.Credentials.from_service_account_file('/path/to/credentials.json')
    drive_service = build('drive', 'v3', credentials=credentials)

    # Set up query to search for image files
    query = "mimeType='image/jpeg' or mimeType='image/png'"

    # Execute the query to retrieve image files
    response = drive_service.files().list(q=query).execute()
    files = response.get('files', [])

    # Download the image files
    for file in files:
        file_id = file['id']
        file_name = file['name']
        file_path = f'/path/to/save/{file_name}'

        request = drive_service.files().get_media(fileId=file_id)
        fh = open(file_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        print(f"Downloaded {file_name} to {file_path}")

