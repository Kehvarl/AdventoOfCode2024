from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


def test(levels):
    safe = True
    fault = 0
    prev = levels[0]
    direction = 0
    for i, level in enumerate(levels[1:]):
        if direction == 0:
            if level > prev:
                direction = 1
            else:
                direction = -1
        else:
            if (level > prev and direction == -1) or (level < prev and direction == 1):
                safe = False
                fault = i + 1
        if (abs(level - prev)) > 3 or (abs(level - prev)) < 1:
            safe = False
            fault = i + 1
        if not safe:
            break
        prev = level
    return safe, fault

safes = 0
for line in content:
    retest = True
    levels = [int(x) for x in line.split()]
    safe, fault = test(levels)
    if safe:
        safes += 1
    else:
        copy = levels.copy()
        for x, val in enumerate(levels):
            l = copy.copy()
            del l[x]
            safe, fault = test(l)
            print(levels, l, fault)
            if safe:
                safes += 1
                break

print(safes)
