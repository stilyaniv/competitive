#!/bin/python2

import sys

# 1.1
# print sum([ int(line.strip()) if line.strip() else 0 for line in sys.stdin ])

# 1.2
found = 0
total = 0
seen = {0 : 1}
freqs = [line.strip() for line in sys.stdin]
while(not(found)):
    for line in freqs:
        if line.strip():
            total += int(line.strip())
            if total in seen:
                print "Seen again:", total
                found = 1
                break
            else:
                seen[total] = 1
if not(found):
    print "No repeats"
