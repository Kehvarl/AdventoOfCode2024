from collections import defaultdict, deque
from pprint import pprint

with open("test.txt") as f:
    # content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]
    i_grid, i_commands = f.read().split("\n\n")

# grid = [l.strip() for l in i_grid.split("\n")]
commands = i_commands.replace("\n", "").strip()

boxes_l = set()
boxes_r = set()
walls = set()
robot = ()
w = 0
h = 0
for y, v1 in enumerate([l.strip() for l in i_grid.split("\n")]):
    x = 0
    for v2 in v1:
        if x > w:
            w = x
        if v2 == "@":
            robot = (x, y)
        elif v2 == "O":
            boxes_l.add((x, y))
            boxes_r.add((x+1, y))
        elif v2 == "#":
            walls.add((x, y))
            walls.add((x+1, y))
        x += 2
    if y > h:
        h = y

w += 1
h += 1
movements = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}


def move(command, robot, boxes_l, boxes_r):
    dx, dy = movements[command]
    rx, ry = robot
    rnx = rx + dx
    rny = ry + dy
    if (rnx, rny) in walls:
        return robot, boxes_l, boxes_r
    elif (rnx, rny) in boxes_l or (rnx, rny) in boxes_r:
        moving = True
        bnx = rnx
        bny = rny
        move_boxes_l = []
        move_boxes_r = []
        new_boxes_l = []
        new_boxes_r = []
        while moving:
            if (bnx, bny) in boxes_l:
                move_boxes_l.append((bnx, bny))
                move_boxes_r.append((bnx + 1, bny))
                bnx = bnx + 1 + dx
                bny = bny + dy
                new_boxes_l.append((bnx, bny))
                new_boxes_r.append((bnx + 1, bny))
            elif (bnx, bny) in boxes_r:
                move_boxes_l.append((bnx - 1, bny))
                move_boxes_r.append((bnx, bny))
                bnx = bnx + dx
                bny = bny + dy
                new_boxes_l.append((bnx - 1, bny))
                new_boxes_r.append((bnx, bny))
            elif (bnx, bny) in walls:
                return robot, boxes_l, boxes_r
            else:
                moving = False

        boxes_l = boxes_l.difference(move_boxes_l).union(new_boxes_l)
        boxes_r = boxes_r.difference(move_boxes_r).union(new_boxes_r)

    return ((rnx, rny), boxes_l, boxes_r)


def print_map(robot, boxes_l, boxes_r, walls, w, h):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in walls:
                line += "#"
            elif (x, y) in boxes_l:
                line += "["
            elif (x, y) in boxes_r:
                line += "]"
            elif (x, y) == robot:
                line += "@"
            else:
                line += "."
        print(line)


for c in range(len(commands)):
    robot, boxes_l, boxes_r = move(commands[c], robot, boxes_l, boxes_r)
    #print(c, commands[c])
    print_map(robot, boxes_l, boxes_r, walls, w, h)

gps = 0
for bx, by in boxes_l:
    #print(100*by, bx)
    gps += (100 * by + bx)

print(gps)