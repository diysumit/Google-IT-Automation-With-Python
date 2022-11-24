#!/usr/bin/env python3

from fileinput import filename
import os
import mimetypes
import smtplib
import getpass

from email.message import EmailMessage

# creating EmailMessage object from email.message module
message = EmailMessage()

sender = 'ss3808@srmist.edu.in'
recipient = 'diysumit@gmail.com'

# setting up sender
message['From'] = sender

# setting up recipient
message['To'] = recipient

sender_name = 'Me'
recipient_name = 'Me'

# setting up subject of email
message['Subject'] = f'Greetings from {sender_name} to {recipient_name}'

# To, From and Subject are examples of email header fields, 
# they are key-value pairs that are used servers to route and display messages
# they are seperate from message body

body = """ Hey there,
    I hope you're doing well, this is the last time I am going to write you.
    Goodbye!

    Yours Truly,
    Myself
"""

# setting up body of email
message.set_content(body)

# In order for the recipient of your message
#  to understand what to do with an attachment, 
# you  need to label the attachment with a MIME type
#  and subtype to tell them what sort of file you’re sending. 
# The Internet Assigned Numbers Authority (IANA) (iana.org) 
# hosts a registry of valid MIME types. 
# If you know the correct type and subtype of the files you’ll be sending, 
# you can use those values directly. If you don't know, you can use the 
# Python mimetypes module to make a good guess!

attachment_path = './pic.png'

attachment_filename = os.path.basename(attachment_path)

# when type of attachment is not known mimetypes module can be used to guess
mime_type, _ = mimetypes.guess_type(attachment_path)

# email needs type and subtype seperately
mime_type, mime_subtype = mime_type.split('/', 1)

# adding attachment to our email
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), 
                           maintype=mime_type, 
                           subtype=mime_subtype,
                           filename=attachment_filename
                           )

# final message with attachment
# print(message)

# creating SMTP mail server on localhost
# mail_server = smtplib.SMTP('localhost')


# This error means that there's no local SMTP server configured. 
# But don't panic! You can still connect to the SMTP server for 
# your personal email address. 
# Most personal email services have instructions for sending email 
# through SMTP; just search for the name of your email service 
# and "SMTP connection settings".
# When setting this up, there are a couple of things that you'll 
# probably need to do: Use a secure transport layer and authenticate 
# to the service using a username and password. Let's see what this
#  means in practice.
# You can connect to a remote SMTP server using Transport Layer 
# Security (TLS). An earlier version of the TLS protocol was called
#  Secure Sockets Layer (SSL), and you’ll sometimes see TLS and SSL
#  used interchangeably. This SSL/TLS is the same protocol that's
#  used to add a secure transmission layer to HTTP, making it HTTPS.
#  Within the smtplib, there are two classes for making connections 
# to an SMTP server: The SMTP class will make a direct SMTP connection,
#  and the SMTP_SSL class will make a SMTP connection over SSL/TLS. Like this:

# creating mail_server for gmail ssl connection
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

# debug to see server's working
mail_server.set_debuglevel(1)

# mail_server uses password and username to identify people
# let's use python module to securely get password
print(f'Username: {sender}')
mail_pass = getpass.getpass('Enter Password: ')

#password
print(mail_pass)

# login into mail server
mail_server.login(sender, mail_pass)

# sending email
mail_server.send_message(message)

# closing server connection
mail_server.quit()
