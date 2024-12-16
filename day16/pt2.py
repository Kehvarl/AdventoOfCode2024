from collections import defaultdict, deque
from pprint import pprint

with open("test.txt") as f:
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
            start = (x, y, 1, 0, [(x, y)], 0)
        elif v2 == "E":
            end = (x, y)


def scan(start, end):
    bfs_q = deque()
    bfs_q.append(start)
    visited = set()
    best = None
    best_steps = []
    while len(bfs_q) > 0:
        x, y, dx, dy, steps, turns = bfs_q.popleft()
        if (x, y) == end:
            if best is None:
                best = len(steps) + (1000 * turns)
                best_steps = steps
            else:
                best = min(best, len(steps) + (1000 * turns))
                best_steps = steps
            #print(steps, turns, len(steps) + (1000 * turns), best)
        if (x, y, dx, dy) in visited:
            continue
        visited.add((x, y, dx, dy))

        tx = x + dx
        ty = y + dy
        if 0 <= ty < len(content) and 0 <= tx < len(content[0]) and content[ty][tx] != "#":
            nsteps = steps.copy()
            nsteps.append((tx, ty))
            bfs_q.append((tx, ty, dx, dy, nsteps, turns))
        for nx, ny, nc in directions[(dx, dy)][1:]:
            bfs_q.append((x, y, nx, ny, steps, turns + 1))

    print(best_steps)
    return best, best_steps

best, best_steps = scan(start, end)

for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if (x, y) in best_steps:
            line += "0"
        else:
            line += v2
    print(line)