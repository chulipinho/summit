from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import logger

from drive import Drive
from mail import Mail

log = logger.get_logger()

SCOPES = ["https://www.googleapis.com/auth/gmail.compose", "https://www.googleapis.com/auth/drive.readonly"]

class GoogleServices:
    def __init__(self):
        self._creds = self._authorize()
        self.mail = Mail(self._creds)
        self.drive = Drive(self._creds)
        
    def _authorize(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secrets.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        return creds

