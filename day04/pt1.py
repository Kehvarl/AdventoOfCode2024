from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


def search(grid, x, y, dx, dy):
    search = "XMAS"
    for i, l in enumerate(search):
        if 0 <= y+(dy*i) < len(grid) and 0 <= x+(dx*i) < len(grid[0]):
            if grid[y+(dy*i)][x+(dx*i)] != search[i]:
                return False
        else:
            return False
    return True

found = 0
matchgrid = []
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            if search(content, x, y, dx, dy):
                found += 1
                for i, l in enumerate("XMAS"):
                        matchgrid.append([y + (dy * i),x + (dx * i)])


for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if [y, x] in matchgrid:
            line += content[y][x]
        else:
            line += "."
    print(line)

print(found)