from collections import defaultdict, deque
from pprint import pprint
from functools import cache

with open("input.txt") as f:
    towels, patterns = f.read().split("\n\n")
    # content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]
towels = towels.split(", ")
designs = [d.strip() for d in patterns.strip().split("\n")]

@cache
def test(design):
    patterns = 0
    for t in towels:
        if design == t:
            patterns += 1
        if design[:len(t)] == t:
            patterns += test(design[len(t):])
    return patterns


possible = 0
for d in designs:
    possible += test(d)

print(possible)
