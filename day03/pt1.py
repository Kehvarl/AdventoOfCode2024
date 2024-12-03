from collections import defaultdict, deque
from pprint import pprint
import re

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]
inst = []
prod = 0
for y, v1 in enumerate(content):
    inst.append(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', v1))
for row in inst:
    for com in row:
        l,r = com.split(',')
        l = int(l[4:])
        r = int(r[:-1])
        prod += (r*l)
print(prod)