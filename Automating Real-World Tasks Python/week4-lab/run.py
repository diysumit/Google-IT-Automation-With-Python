#!/usr/bin/env python3

import fruit_dict
import json
import requests
import tiff_to_jpeg

tiff_to_jpeg.ttj()
fruit_dictionary = fruit_dict.process_file()

fruit_jsonObj = json.dumps(fruit_dictionary)

print(fruit_jsonObj)

url = 'http://[linux-instance-external-IP]/fruits'

requests.post(url, json=fruit_jsonObj)