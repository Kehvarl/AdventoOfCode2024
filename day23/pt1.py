from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

graph = defaultdict(list)
for y, v1 in enumerate(content):
    a, b = v1.split("-")
    graph[a].append(b)
    graph[b].append(a)


sets = set()
for a in graph:
    for b in graph[a]:
        both = []
        for c in graph[b]:
            if c in graph[a]:
                both.append(sorted([a, b, c]))
        for s in both:
            for c in s:
                if c[0] == 't':
                    sets.add(tuple(s))
                    break
print(sets)
print(len(sets))

