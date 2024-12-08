from collections import defaultdict, deque
from pprint import pprint
from itertools import combinations

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


allnodes = set()
nodes = defaultdict(set)
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if v2 != '.':
            nodes[v2].add((x, y))
            if v2 != "#":
                allnodes.add((x, y))


def check_node(node):
    x, y = node
    return (0 <= y < len(content)) and \
           (0 <= x < len(content[0]))


def get_antinode(a, b):
    x1, y1 = a
    x2, y2 = b
    odx = dx = abs(x1 - x2)
    ody = dy = abs(y1 - y2)
    n1 = (x1 + dx, y1 + dy) # ++, --
    n2 = (x1 + dx, y1 - dy) # +-, -+
    n3 = (x1 - dx, y1 + dy) # -+, +-
    n4 = (x1 - dx, y1 - dy) # --, ++
    out_nodes = []
    if n1 == b:
        while check_node((x1 - dx, y1 - dy)):
            out_nodes.append((x1 - dx, y1 - dy))
            dx += odx
            dy += ody
    elif n2 == b:
        while check_node((x1 - dx, y1 + dy)):
            out_nodes.append((x1 - dx, y1 + dy))
            dx += odx
            dy += ody
    elif n3 == b:
        while check_node((x1 + dx, y1 - dy)):
            out_nodes.append((x1 + dx, y1 - dy))
            dx += odx
            dy += ody
    elif n4 == b:
        while check_node((x1 + dx, y1 + dy)):
            out_nodes.append((x1 + dx, y1 + dy))
            dx += odx
            dy += ody
    return out_nodes


antinodes = set()
type_antinodes = defaultdict(set)
for n in nodes:
    if n == "#":
        continue
    for subset in combinations(nodes[n], 2):
        a, b = subset
        an = get_antinode(a, b)
        antinodes.update(an)
        an = get_antinode(b, a)
        antinodes.update(an)


for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if (x, y) in antinodes or (x,y) in nodes:
            if v2 != ".":
                line += "@"
            else:
                line += "$"
        else:
            line += v2
    print(line)

print(antinodes)
_n = set()
_n.update(antinodes)
_n.update(allnodes)
print(len(_n))