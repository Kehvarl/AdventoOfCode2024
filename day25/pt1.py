from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip().split("\n") for x in f.read().split("\n\n")]
    # content = [int(x) for x in f.readlines()]

#print(content)

locks = []
lock_codes = []
keys = []
key_codes = []
for schematic in content:
    if schematic[0] == "#####" and schematic[-1] == ".....":
        locks.append(schematic)
        cols = [0,0,0,0,0]
        for line in schematic[1:]:
            for i, char in enumerate(line):
                if char == "#":
                    cols[i] += 1
        lock_codes.append(cols)
    elif schematic[0] == "....." and schematic[-1] == "#####":
        keys.append(schematic)
        cols = [0,0,0,0,0]
        for line in schematic[:-1]:
            for i, char in enumerate(line):
                if char == "#":
                    cols[i] += 1
        key_codes.append(cols)

matches = defaultdict(list)
match_count = 0
for lock in lock_codes:
    for key in key_codes:
        good = True
        for t,l in enumerate(key):
            if l + lock[t] > 5:
                good = False
                break
        if good:
            print(lock, key)
            match_count += 1
            matches[tuple(lock)].append(key)

print(matches)
print(match_count)
#print(locks)
#print(lock_codes)
#print(keys)
#print(key_codes)
#print(matches)
