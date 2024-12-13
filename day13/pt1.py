from collections import defaultdict, deque
from pprint import pprint

with open("test.txt") as f:
    content = f.read().strip().split("\n\n")
    # content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

machines = []
for m in content:
    a, b, p = m.split("\n")
    ax, ay = a[9:].strip().split(", ")
    bx, by = b[9:].strip().split(", ")
    px, py = p[7:].strip().split(", ")
    ba = (int(ax[2:]), int(ay[2:]))
    bb = (int(bx[2:]), int(by[2:]))
    pr = (int(px[2:]), int(py[2:]))

    machines.append([ba, bb, pr])

a_tokens = 0
b_tokens = 0
for ba, bb, pr in machines:
    ax, ay = ba
    bx, by = bb
    px, py = pr
    a = (px * by - py * bx) / (ax * by - ay * bx)
    if a == int(a):
        b = (py - ay * a) // by
        a_tokens += int(a)
        b_tokens += int(b)

print(a_tokens * 3 + b_tokens)
