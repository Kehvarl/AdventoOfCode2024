from collections import defaultdict, deque
from pprint import pprint
import re

with open("input.txt") as f:
    r, p = f.read().split("\n\n")# = [x.strip() for x in f.readlines()
    # content = [int(x) for x in f.readlines()]

updates_ = p.strip().split("\n")
updates = []
for line in updates_:
    updates.append([int(x.strip()) for x in line.split(",")])

rules_ = [x.strip() for x in r.split("\n")]
rules = defaultdict(list)
for rule in rules_:
    a, b = rule.split("|")
    rules[int(a)].append(int(b))

good = []
for u in updates:
    valid = True
    for i, v in enumerate(u):
        for ii, vv in enumerate(u[i:]):
            if v in rules[vv]:
                valid = False
                break
    if valid:
        good.append(u[len(u)//2])
print(good)
print(sum(good))