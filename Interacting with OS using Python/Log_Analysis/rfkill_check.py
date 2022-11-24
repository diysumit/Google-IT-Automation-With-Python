#!/usr/bin/env python3

import re
import operator
import csv

frequency_of_error = {}
entries_for_users = {}

file = open('syslog.log', 'r')
for line in file.readlines():
    if re.search(r'Warning', line):
        format = re.compile(r'([\w]+): ([\w.-]+)')
        groups = re.search(format, line)
        key = groups[2]
        if key not in frequency_of_error.keys():
            frequency_of_error[key] = 1
        else:
            frequency_of_error[key] += 1
print(frequency_of_error)
file.close()
with open('report.csv', 'x') as file:
    fieldnames = ['systemd-rfkill.service', 'systemd-rfkill.socket']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(frequency_of_error)
