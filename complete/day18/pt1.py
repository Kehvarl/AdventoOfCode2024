from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

blocks = []
for line in content:
    x, y = [int(l) for l in line.split(",")]
    blocks.append((x, y))



def get_lowest_neighbor_value(grid, corrupted, x, y, w, h):
    lowest = w * h + 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if (tx, ty) in corrupted:
            continue
        if 0 <= (tx) < w and 0 <= (ty) < h:
            lowest = min(lowest, grid[(tx, ty)])
    return lowest

w = 71
h = 71

corrupted = blocks[:1024]
grid = defaultdict(lambda: w * h + 1)
grid[(w-1, h-1)] = 0
changed =True
while changed:
    changed = False
    for y in range(h):
        for x in range(w):
            lowest_neighbor = get_lowest_neighbor_value(grid, corrupted, x, y, w, h)
            if grid[(x, y)] > lowest_neighbor + 1:
                grid[(x, y)] = lowest_neighbor + 1
                changed = True

def print_map(w, h, corrupted):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in corrupted:
                if (x, y) in outpath:
                    line += "!"
                else:
                    line += "#"
            elif (x, y) in outpath:
                line += "0"
            else:
                line += "."
        print(line)

def print_grid(grid, w, h, corrupted):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in corrupted:
                line += "#"
            else:
                line += str(grid[(x, y)])
        print(line)

print_grid(grid, w, h, corrupted)
print(grid[(0,0)])