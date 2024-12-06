from collections import defaultdict, deque
from pprint import pprint

with open("test.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


visited = set()
barricades = []
hit = []

loop = set()
guard = []
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if v2 == '^':
            guard = [x, y, 0]
            visited.add((x, y))
        elif v2 == '#':
            barricades.append([x, y])

on_map = True
while on_map:
    nx = guard[0] + directions[guard[2]][0]
    ny = guard[1] + directions[guard[2]][1]
    if [nx, ny] in barricades:
        guard[2] = (guard[2] + 1) % 4
        hit.append([nx, ny])
    else:
        if 0 <= nx < len(content[0]) and 0 <= ny < len(content):
            guard = [nx, ny, guard[2]]
            nb = None
            for b in barricades:
                bx, by = b
                if guard[2] == 0 and by == ny and bx > nx:
                    nb = [nx + directions[guard[2]][0], ny + directions[guard[2]][1]]
                elif guard[2] == 1 and bx == nx and by < ny:
                    nb =[nx + directions[guard[2]][0], ny + directions[guard[2]][1]]
                elif guard[2] == 2 and by == ny and bx < nx:
                    nb = [nx + directions[guard[2]][0], ny + directions[guard[2]][1]]
                elif guard[2] == 3 and bx == nx and bx > nx:
                    nb = [nx + directions[guard[2]][0], ny + directions[guard[2]][1]]
                if nb is not None and nb not in barricades and b in hit:
                    loop.add(tuple(nb))

            visited.add((nx, ny))
        else:
            on_map = False


for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if (x, y) in loop:
            line += "0"
        elif (x,y) in visited:
            line += "X"
        else:
            line += v2
    print(line)


print(len(visited))
print(len(loop))
