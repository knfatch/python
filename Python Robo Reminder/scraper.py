# Email scraping file for 'Python Robo Reminder' app
Version = 1.3
#-------Imports----------
import requests     #Used to fetch emails/content
import re           #Used to search for patterns
import imaplib      #Used for read, search and downloading email messages
import ssl          #Used for secure conection to email
import email        #Used for email parsing
from email.header import decode_header    #Used for filtering by a specific sender
from reminder import app_pass, sender    #Variables from 'reminder.py' for email and app password

#--------Functions-------

#--------Main------------
context = ssl.create_default_context()      #Used to help verify certificates when connecting to email service

with imaplib.IMAP4_SSL('imap.gmail.com', port=993, ssl_context=context) as mail:
    mail.login(sender, app_pass)
    mail.select('inbox')

    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    res, msg_data = mail.fetch(email_ids[-1], '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            print(f'Subject: {msg['subject']};)')