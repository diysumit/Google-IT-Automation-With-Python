#!/usr/bin/env python3

import re
#import sys

def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    if result is None:
        return name
    return f'{result[2]} {result[1]}'

#name = sys.argv[1] + ', ' + sys.argv[2]
#print(rearrange_name(name))
