import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import logger

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

log = logger.get_logger()

class Mail:
    def __init__(self, creds):
        self._service = self._build_service(creds)
    
    def _build_service(self, creds):
        return build('gmail', 'v1', credentials=creds)

    def _create_message(self, content, subject, to):
        message = EmailMessage()

        message.set_content(content)

        message["To"] = to
        message["From"] = "summit@app.com"
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

            log.info(f"E-mail sent to {', '.join(to)} successfully")

        except HttpError as error:
            print(f"An error occurred: {error}")
            send_message = None

        return send_message

if __name__ == "__main__":
    pass