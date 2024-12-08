from collections import defaultdict, deque
from pprint import pprint
from itertools import combinations

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


nodes = defaultdict(list)
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if v2 != '.':
            nodes[v2].append((x, y))

print(nodes)


def check_node(node):
    x, y = node
    return (0 <= y < len(content)) and \
           (0 <= x < len(content[0]))


def get_antinode(a, b):
    x1, y1 = a
    x2, y2 = b
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    n1 = (x1 + dx, y1 + dy) # ++, --
    n2 = (x1 + dx, y1 - dy) # +-, -+
    n3 = (x1 - dx, y1 + dy) # -+, +-
    n4 = (x1 - dx, y1 - dy) # --, ++
    if n1 == b:
        return n4
    elif n2 == b:
        return n3
    elif n3 == b:
        return n2
    elif n4 == b:
        return n1


antinodes = set()
type_antinodes = defaultdict(list)
for n in nodes:
    if n == "#":
        continue
    for subset in combinations(nodes[n], 2):
        a, b = subset
        an = get_antinode(a, b)
        if check_node(an):
            antinodes.add(an)
        an = get_antinode(b, a)
        if check_node(an):
            antinodes.add(an)

print(antinodes)
for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if (x, y) in antinodes:
            if v2 != ".":
                line += "@"
            else:
                line += "$"
        else:
            line += v2
    print(line)

print(len(antinodes))