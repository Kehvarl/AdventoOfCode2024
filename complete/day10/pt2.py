from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

trailheads = []
endpoints = []
trailmap = {}

for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if v2 != '.':
            trailmap[(x, y)] = int(v2)
        if v2 == '.':
            continue
        elif int(v2) == 0:
            trailheads.append((x, y))
        elif int(v2) == 9:
            endpoints.append((x, y))


def walk(trailhead, trailmap):
    score = 0
    rating = 0
    bfs_q = deque()
    bfs_q.append(trailhead)
    visited = set()

    while len(bfs_q) > 0:
        x, y = bfs_q.popleft()
        curval = trailmap[(x, y)]
        if curval == 9:
            rating += 1
            if (x, y) not in visited:
                score += 1
        visited.add((x, y))

        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if trailmap.get((x + nx, y + ny)) == curval + 1:
                #print((x, y, curval), (x + nx, y + ny, trailmap.get((x + nx, y + ny))))
                bfs_q.append((x + nx, y + ny))

    return score, rating


score = 0
rating = 0
for t in trailheads:
    s, r = walk(t, trailmap)
    score += s
    rating += r

print(score, rating)
