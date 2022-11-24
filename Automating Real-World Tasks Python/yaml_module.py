#!/usr/bin/env python3

import yaml

# let's take a list of dictionaries
sample = [
{
    'Phone': {
        'Home' : '254-257-2415'
    }
}, 
{
    'Phone': {
        'Home' : '241-236-2415',
        'Office' : '214-232-2541'
    }
}, 
]

# and dump that into a sample2.yaml file
with open('sample2.yaml', 'w') as sample2_yaml:
    yaml.safe_dump(sample, sample2_yaml)