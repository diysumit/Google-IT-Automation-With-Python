#!/usr/bin/env python3

import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as file:
    for line in file:
        if "ERROR" not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        print(result[1])

print(usernames)
