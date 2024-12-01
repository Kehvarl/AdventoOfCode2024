from collections import defaultdict, deque
import itertools
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

left = []
right = []

for v1 in content:
    l, r = v1.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()
combined = zip(left, right)
diffs = []
for c in combined:
    diffs.append(abs(int(c[1]) - int(c[0])))
print(diffs)
print(sum(diffs))


