from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


end = ()
start = ()
directions = {
    (1,  0): [(1, 0, 1), (0, 1, 1000), (0, -1, 1000)],
    (-1, 0): [(-1, 0, 1), (0, 1, 1000), (0, -1, 1000)],
    (0,  1): [(0, 1, 1), (1, 0, 1000), (-1, 0, 1000)],
    (0, -1): [(0, -1, 1), (1, 0, 1000), (-1, 0, 1000)]
}

for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if v2 == "S":
            start = (x, y, 1, 0, 0, 0)
        elif v2 == "E":
            end = (x, y)


def scan(start, end):
    bfs_q = deque()
    bfs_q.append(start)
    visited = set()
    best = None
    while len(bfs_q) > 0:
        x, y, dx, dy, steps, turns = bfs_q.popleft()
        if (x, y) == end:
            if best is None:
                best = steps + (1000 * turns)
            else:
                best = min(best, steps + (1000 * turns))
            print(steps, turns, steps + (1000 * turns), best)
        if (x, y, dx, dy) in visited:
            continue
        visited.add((x, y, dx, dy))

        tx = x + dx
        ty = y + dy
        if 0 <= ty < len(content) and 0 <= tx < len(content[0]) and content[ty][tx] != "#":
            bfs_q.append((tx, ty, dx, dy, steps + 1, turns))
        for nx, ny, nc in directions[(dx, dy)][1:]:
            bfs_q.append((x, y, nx, ny, steps, turns + 1))

    return best

print(scan(start, end))
