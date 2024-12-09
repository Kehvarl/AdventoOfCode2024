from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()][0]
    # content = [int(x) for x in f.readlines()]

files = []
empty = []

file = True
fi = 0
for y, v1 in enumerate(content):
    if file:
        files.extend([fi]*int(v1))
        file = False
    else:
        empty.extend([(len(files) + i) for i in range(int(v1))])
        files.extend(['.']*int(v1))
        file = True
        fi += 1


for b in range(len(files)-1, -1, -1):
    if files[b] != '.' and len(empty) > 0 and b > empty[0]:
        address = empty.pop(0)
        files[address] = files[b]
        files[b] = '.'

cs = 0
for y, v1 in enumerate(files):
    if v1 != '.':
        cs += (y * int(v1))
print(cs)

