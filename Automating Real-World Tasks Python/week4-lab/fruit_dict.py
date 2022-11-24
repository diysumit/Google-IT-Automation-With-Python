#!/usr/bin/env python3

import os
import requests
import sys
import json

def process_file(description_path='/home/diysumit/supplier-data/descriptions/', image_path='/home/diysumit/supplier-data/images/'):
    """
    Returns a processed dictionary 

    {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}

    def process_file(description_path='~/supplier-data/descriptions/', image_path='~/supplier-data/images/'):
    fruits = []
    image_name = []
    for file in os.listdir(description_path):
        if file.endswith('.txt'):
            with open(description_path+file, 'r') as text_file:
                lines = text_file.readlines()
                fruit = {
                            "name" : lines[0][:-1], 
                            "weight" : lines[1][:-1], 
                            "description" : lines[2],
                            }
                fruits.append(fruit)
    for file in os.listdir(image_path):
        if file.endswith('.jpeg'):
            image_name.append(file)
    for i in range(len(image_name)):
        fruits[i]['image_name'] = image_name[i]
    return fruits


    """
    fruits = []
    image_name = []
    for file in os.listdir(description_path):
        if file.endswith('.txt'):
            with open(description_path+file, 'r') as text_file:
                lines = text_file.readlines()
                fruit = {
                            "name" : lines[0][:-1], 
                            "weight" : lines[1][:-1], 
                            "description" : lines[2][:-1],
                            }
                fruits.append(fruit)

    for file in os.listdir(image_path):
        if file.endswith('.jpeg'):
            image_name.append(file)
    for i in range(len(image_name)):
        fruits[i]['image_name'] = image_name[i]
    return fruits
