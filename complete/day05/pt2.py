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

def check(update):
    for i, v in enumerate(update):
        for ii, vv in enumerate(update[i:]):
            if v in rules[vv]:
                return False
    return True

def repair(update):
    repaired = update.copy()
    for i in range(len(repaired)-1, -1, -1):
        for ii in range(i, -1, -1):
            if repaired[i] in rules[repaired[ii]]:
                swap = repaired.pop(ii)
                repaired.insert(i, swap)

    return repaired

good = []
bad = []
repaired = []
for u in updates:
    valid = True
    if not check(u):
        valid = False
        r = repair(u)

    if valid:
        good.append(u[len(u)//2])
    else:
        bad.append(r[len(r)//2])

print(good)
print(sum(good))
print(bad)
print(sum(bad))
