#%%
# from __future__ import print_function
from googleapiclient.discovery import build
import os
#
from utils.utils import auth, send_email, get_labels
from utils.utils import send_email



#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = 'https://mail.google.com/'
credential_path = os.path.join(os.getcwd(), 'config', 'credentials.json')

authIst = auth(SCOPES)
creds = authIst.get_credentials(credential_path)
service = build('gmail', 'v1', credentials=creds)
get_labels(service)

send_my_first_email = send_email(service)

sender = 'sergiomarreromarrero@gmail.com'
to = 'sergiomarreromarrero@gmail.com'
subject = 'Hello World'
message_text = 'Message from python'

a_message = send_my_first_email.create_message(sender, to , subject, message_text)
a_message


send_my_first_email.send_message(user_id='sergiomarreromarrero@gmail.com', message=a_message['raw'].decode())

