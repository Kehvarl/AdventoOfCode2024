from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

safes = 0
for line in content:
    levels = [int(x) for x in line.split()]
    safe = True
    prev = levels[0]
    direction = 0
    for level in levels [1:]:
        if direction == 0:
            if level > prev:
                direction = 1
            else:
                direction = -1
        else:
            if (level > prev and direction == -1) or (level < prev and direction == 1):
                safe = False
        if (abs(level - prev)) > 3 or (abs(level - prev)) < 1:
            safe = False
        if not safe:
            break
        prev = level
    if safe:
        safes += 1

print(safes)


