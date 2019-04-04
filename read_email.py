from __future__ import print_function
import httplib2
from pprint import pprint

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

import json
import base64

import Email

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
class read_email:
    def __init__(self, service):
        self.service = service
    def read_email(self, user_id):
        results = self.service.users().messages().list(userId=user_id, labelIds = ['INBOX']).execute()
        messages = results.get('messages', [])

        if not messages:
            print('No messages detected.')
            return None
        else:
            for message in messages:
                msg = self.service.users().messages().get(userId = user_id, id = message['id']).execute()
                headers = msg['payload']['headers']

                msg_from = ""
                msg_to = "" 
                msg_subject = "" 
                msg_reference = ""
                msg_in_reply_to = ""
                msg_id = msg['id']
                msg_body = ""
                msg_thread_id = msg['threadId']

                for header in headers:
                    if str.lower(header['name']) == 'from':
                        msg_from = header['value']
                    if str.lower(header['name']) == 'to':
                        msg_to = header['value']
                    if str.lower(header['name']) == 'subject':
                        msg_subject = header['value']
                    if header['name'] == 'In-Reply-To':
                        msg_in_reply_to = header['value']
                    if header['name'] == 'References':
                        msg_reference = header['value']
                    else:
                        pass
                    
                try:
                    parts = msg['payload']['parts']
                    part_body = parts[0]['body']['data']
                    msg_body = base64.urlsafe_b64decode(part_body).decode()
                except:
                    pass
                
                email = Email.Email(msg_to,msg_from, msg_in_reply_to, msg_reference, msg_subject, msg_body, msg_id, msg_thread_id)
                print(email)
            return email