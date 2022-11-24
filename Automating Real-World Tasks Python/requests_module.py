#!/usr/bin/env python3

from distutils.dep_util import newer
import requests

response = requests.get('https://www.google.com')

# text of response HTML page
print(response.text[:300])

print('/n')

# raw response given by server
print(response.raw.read()[:300])

# check if content what kind of response from server was acceptable
print(response.request.headers['Accept-Encoding'])

print('/n')

# check if content was encoded
print(response.request.headers['Content-Encoding'])

print('/n')

# True if response made was successfull
print(response.ok)

print('/n')

# status code of response
print(response.status_code)

print('/n')

# url of request made from response
print(response.request.url)

# parameter that can be passed along with url in get request
p = {"search": "grey kitten",  "max_results": 15}

# we can make post request too with above data
new_response = requests.post('https://www.google.com', data=p)


print('/n')

print(new_response.request.url)

print('/n')

# response body
print(new_response.request.body)

# it's common to use json parameter when making post request
newer_response = requests.post('https://www.google.com', json=p)

# printing url and body

print(newer_response.request.url)

print('/n')

print(newer_response.request.body)