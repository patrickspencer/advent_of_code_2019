"""
Day 4 Part 1
~~~~~~~~~~~~
"""

from collections import Counter

def check_num(num):
    s = str(num)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    if all(i < 2 for i in Counter(s).values()): 
       return False
    return True

a = 0
for i in range(240920,789858):
    if check_num(i):
        a += 1

print(a)