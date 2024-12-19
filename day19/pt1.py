from collections import defaultdict, deque
from pprint import pprint
from queue import Queue

with open("input.txt") as f:
    towels, patterns = f.read().split("\n\n")
    # content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

towels = towels.split(", ")

designs = [d.strip() for d in patterns.strip().split("\n")]


def test(design, towels):
    for t in towels:
        if design == t:
            return True
        if design[:len(t)] == t and test(design[len(t):], towels):
            return True
    return False


possible = 0
for d in designs:
    if test(d, towels):
        possible += 1
print(possible)

print(possible)