import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

import os 
import logger

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

log = logger.get_logger()

class Mail:
    def __init__(self, email=""):
        self._creds = self._authorize()
        self._service = self._build_service(self._creds)
        self.email_address = email

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
    
    def _build_service(self, creds):
        service = build('gmail', 'v1', credentials=creds)
        return service

    def _create_message(self, content, subject, to):
        message = EmailMessage()

        message.set_content(content)

        message["To"] = to
        message["From"] = self.email_address
        message["Subject"] = subject
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        return {"raw": encoded_message}

    def send(self, content, subject, to):
        try:
            message = self._create_message(content, subject, to)

            send_message = (
                self._service.users()
                .messages()
                .send(userId="me", body=message)
                .execute()
            )

            log.info("E-mail sent successfully")

        except HttpError as error:
            print(f"An error occurred: {error}")
            send_message = None

        return send_message

if __name__ == "__main__":
    pass