#!/bin/python2

import sys
from string import ascii_lowercase

# 2.1
'''
twos = 0
threes = 0
for line in sys.stdin:
    line_dict = dict.fromkeys(ascii_lowercase, 0)
    for char in line.strip():
       line_dict[char] += 1 
    f3 = 0
    f2 = 0
    for k in line_dict:
        if f2 and f3:
            break
        if not(f3) and line_dict[k] == 3:
            threes += 1
            f3 = 1
        if not(f2) and line_dict[k] == 2:
            twos += 1
            f2 += 1
print(twos * threes)
'''

# 2.2
unicorn = 'asgwjcmbrkedihqoutfylvzpnx' 
lines = [line.strip() for line in sys.stdin]
copy_lines = lines
for line in lines:
    for copy in copy_lines:
        if line != copy:
            count = 0
            for c1,c2 in zip(line,copy):
                if count > 1:
                    break
                if c1 != c2:
                    count +=1 
            if count == 1:
                print line
                print copy
                break
    

'''
for line in sys.stdin:
    for i in range(26):
        if line[i] != unicorn[i]:
            print(1),
    print('')
print(lines)
'''
