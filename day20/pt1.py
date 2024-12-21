from collections import defaultdict, deque
from pprint import pprint
from queue import Queue

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

grid = defaultdict(int)
walls = set()
start = None
end = None
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        grid[(x, y)] == v2
        if v2 == "#":
            walls.add((x, y))
        elif v2 == "S":
            start = (x, y)
        elif v2 == "E":
            end = (x, y)


def bfs(walls, start, end,  w, h):
    bfs_q = Queue()
    bfs_q.put((start, [(start)]))
    visited = set()
    visited.add(start)

    while not bfs_q.empty():
        pos, path = bfs_q.get()
        x, y, = pos

        if (x, y) == end:
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = x + dx, y + dy
            ttx = x + (dx * 2)
            tty = y + (dy * 2)
            if (0 <= ty < h and 0 <= tx < w) and ((tx, ty) not in visited) and (tx, ty) not in walls:
                bfs_q.put(((tx, ty), path + [(tx, ty)]))
                visited.add((tx, ty))
    return None


def draw_map():
    for y, v1 in enumerate(content):
        line = ""
        for x, v2 in enumerate(v1):
            if (x, y) in path and v2 not in ["E", "S"]:
                line += "O"
            else:
                line += v2
        print(line)


path = bfs(walls, start, end, len(content[0]), len(content))
print(len(path))

skips = 0

count = 0
for i,j in path:
    for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
        if (i+di,j+dj) not in path and (i+2*di,j+2*dj) in path and path[(i+2*di,j+2*dj)]-path[(i,j)]>=102:
            count += 1
print(skips)
