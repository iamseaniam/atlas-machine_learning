#!/usr/bin/python2.7
"""documentation"""
import sys


for line in sys.stdin:
    line = line.strip()
    fields = line.split(",")

    if fields[0] == "id":
        continue

    if len(fields) >= 3:
        id = fields[0]
        company = fields[1]
        total_yearly_compensation = fields[3]
        print "{}\t{},{}".format(id, company, total_yearly_compensation)
