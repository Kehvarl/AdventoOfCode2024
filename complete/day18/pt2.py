from collections import defaultdict, deque
from queue import Queue
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

blocks = []
for line in content:
    x, y = [int(l) for l in line.split(",")]
    blocks.append((x, y))


def bfs(corrupted, x, y, w, h):
    bfs_q = Queue()
    bfs_q.put((x, y, [(x, y)]))
    visited = set()
    visited.add((x, y))

    while not bfs_q.empty():
        x, y, path = bfs_q.get()

        if (x, y) == (w-1, h-1):
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = x + dx, y + dy
            if (0 <= ty < h and 0 <= tx < w) and ((tx, ty) not in corrupted) and ((tx, ty) not in visited):
                bfs_q.put((tx, ty, path + [(tx, ty)]))
                visited.add((tx, ty))
    return None


def draw_map(w, h, path, blocks):
    broken = []
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in blocks:
                if path is not None and (x, y) in path:
                    line += "!"
                    broken.append((x, y))
                else:
                    line += "#"
            elif path is not None and (x, y) in path:
                line += "0"
            else:
                line += "."
        print(line)
    print(broken)


w = 71
h = 71
path = None
for i, b in enumerate(blocks):
    if i > 1024:
        path = bfs(blocks[:i], 0, 0, w, h)

        if i == 1025:
            print(len(path) - 1)
        if not path:
            print(i, b)
            break
