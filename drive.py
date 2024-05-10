from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import io
import logger

log = logger.get_logger()

class Drive:
    def __init__(self, creds):
        self._service = self._build_service(creds)
    
    def _build_service(self, creds):
        return build("drive", "v3", credentials=creds)

    def _get_folder_id(self, path):
        folder_path = path.split("/")
        folder_id = None
        
        for name in folder_path:
            query = f"mimeType = 'application/vnd.google-apps.folder' and name = '{name}'"
            if folder_id:
                query += f" and '{folder_id}' in parents"
            else: 
                query += " and 'root' in parents"

            try:
                folders = self._service.files().list(q=query, fields="files(id, name)").execute()["files"]
            except Exception as err:
                print(f"Error looking for folder {name}: {err}")
                exit()

            if len(folders) == 0:
                print(f"Folder {name} not found")
                exit()

            folder_id = folders[0]["id"]
            
        return folder_id
        
    def get_content(self, path, mime_type=None):
        log.info(f"Getting content from {path}")
        folder_id = self._get_folder_id(path)

        query = f"'{folder_id}' in parents"
        if mime_type:
            query += f" and mimeType contains '{mime_type}'"

        try:
            res = self._service.files().list(q=query).execute()
        except Exception as err:
            log.error(f"Error reading files from {path}: {repr(err)}")
            exit(0)

        return res["files"]
    
    def download_file(self, file_id, path):
        request = self._service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Downloading video %d%%." % int(status.progress() * 100))

        with open(path, "wb") as f:
            f.write(file.getbuffer())