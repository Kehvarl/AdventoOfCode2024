from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


def scan(plot, garden, visited):
    bfs_q = deque()
    bfs_q.append(plot)
    region = [plot]
    region_perimeter = 0

    while len(bfs_q) > 0:
        x, y = bfs_q.popleft()
        curval = garden[y][x]
        visited.append((x, y))
        perimeter = 4
        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + nx
            ty = y + ny
            if 0 <= ty < len(garden) and 0 <= tx < len(garden[0]):
                if garden[ty][tx] == curval:
                    perimeter -= 1
                    if (tx, ty) not in visited and (tx, ty) not in bfs_q:
                        bfs_q.append((tx, ty))
                        region.append((tx, ty))
        region_perimeter += perimeter
    return region, region_perimeter



regions = []
region_perimeters = []
total = 0
visited = []

for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if (x,y) not in visited:
            (r, p) = scan((x, y), content, visited)
            regions.append(r)
            region_perimeters.append(p)
            total += len(r) * p

pprint(regions)
pprint(region_perimeters)
print(total)

