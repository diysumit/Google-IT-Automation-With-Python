#!/usr/bin/env python3

import json

# let's take a list of dictionaries
sample = [
  "apple",
  "banana",
  12345,
  67890,
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  }
]


# and write that dump that list of dictonaries in a sample2.json file
# without indent parameter file will be written in one line
with open('sample2.json', 'w') as sample2_json:
    json.dump(sample, sample2_json, indent=4)

# dumps method serializes data but instead of writing in file it returns string
sample_string = json.dumps(sample)

print(type(sample_string))
print(sample_string)

# to deserialize json_string objects like above we need to use json.loads()

ObjFromString = json.loads(sample_string)

print(type(ObjFromString))
print(ObjFromString)

# to deserialize json_file objects we need to use json.load()

with open('sample2.json', 'r') as sample2_json:
    ObjFromFile = json.load(sample2_json)
    print(type(ObjFromFile))
    print(ObjFromFile)