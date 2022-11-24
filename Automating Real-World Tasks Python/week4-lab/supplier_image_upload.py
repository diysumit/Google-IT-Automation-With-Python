#!/usr/bin/env python3

import requests
import os

def upload_images(url='http://localhost/upload', file_location='~/supplier-data/images/'):
    """
    Uploads a file to given server location in binary format

    def upload_images(url='http://localhost/upload', file_location='.'):
        for file in os.listdir(file_location):
            with open(file_location+file, 'rb') as opened_file:
                r = requests.post(url=url, files={'file': opened_file})
    
    """
    for file in os.listdir(file_location):
        with open(file_location+file, 'rb') as opened_file:
            # sending file data to server in binary format as a dictionary
            r = requests.post(url=url, files={'file': opened_file})