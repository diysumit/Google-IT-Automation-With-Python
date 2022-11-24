#!/usr/bin/env python3

import os
import requests
import sys
import json
from multiprocessing import Pool

def process_file(path):
    """Returns a dictionary prcossed to be written"""
    feedbacks = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(file, 'r') as text_file:
                lines = text_file.readlines()
                feedback = {
                            "title" : lines[0][:-1], 
                            "name" : lines[1][:-1], 
                            "date" : lines[2][:-1], 
                            "feedback" : lines[3],
                            }
                feedbacks.append(feedback)
    return feedbacks

def post_feedbacks(feedbacks):
    url = "https://httpbin.org/post"
    for feedback in feedbacks:
        response = requests.post(url, json=json.dumps(feedback))
        response.raise_for_status()

def main():
    try:
        feedbacks = process_file('.')
        p = Pool(len(feedbacks))
        p.map(post_feedbacks, feedbacks)
    except Exception as e:
        print(f"Exception Occured: {e}")

if __name__ == "__main__":
    sys.exit(main())