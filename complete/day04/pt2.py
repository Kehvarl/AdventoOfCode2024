from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


def search(grid, x, y, dx, dy):
    search = "MAS"
    for i, l in enumerate(search):
        if 0 <= y+(dy*i) < len(grid) and 0 <= x+(dx*i) < len(grid[0]):
            if grid[y+(dy*i)][x+(dx*i)] != search[i]:
                return False
        else:
            return False
    return True

def check(grid, x, y):
    m1 = grid[y-1][x-1]
    m2 = grid[y-1][x+1]
    a = grid[y][x]
    s1 = grid[y+1][x+1]
    s2 = grid[y+1][x-1]
    if (m1 == "M" and s1 == "S") or (m1 == "S" and s1 == "M"):
        if (m2 == "M" and s2 == "S") or (m2 == "S" and s2 == "M"):
            return True
    return False


found = 0
matchgrid = []
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if content[y][x] == "A":
            if 0 <= y-1 and y + 1 < len(content) and \
               0 <= x-1 and x + 1 < len(content[0]):
                if check(content, x, y):
                    found += 1
                    matchgrid.append([y - 1, x - 1])
                    matchgrid.append([y - 1, x + 1])
                    matchgrid.append([y, x])
                    matchgrid.append([y + 1, x - 1])
                    matchgrid.append([y + 1, x + 1])


for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if [y, x] in matchgrid:
            line += content[y][x]
        else:
            line += "."
    print(line)
print(found)