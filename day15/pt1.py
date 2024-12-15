from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    # content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]
    i_grid, i_commands = f.read().split("\n\n")

# grid = [l.strip() for l in i_grid.split("\n")]
commands = i_commands.replace("\n", "").strip()

boxes = set()
walls = set()
robot = ()
w = 0
h = 0
for y, v1 in enumerate([l.strip() for l in i_grid.split("\n")]):
    for x, v2 in enumerate(v1):
        if x > w:
            w = x
        if v2 == "@":
            robot = (x, y)
        elif v2 == "O":
            boxes.add((x, y))
        elif v2 == "#":
            walls.add((x, y))
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


def move(command, robot, boxes):
    dx, dy = movements[command]
    rx, ry = robot
    rnx = rx + dx
    rny = ry + dy
    if (rnx, rny) in walls:
        return robot, boxes
    elif (rnx, rny) in boxes:
        move_boxes = [(rnx, rny)]
        bnx = rnx + dx
        bny = rny + dy
        new_boxes = [(bnx, bny)]
        moving = True
        while moving:
            if (bnx, bny) in boxes:
                move_boxes.append((bnx, bny))
                bnx = bnx + dx
                bny = bny + dy
                new_boxes.append((bnx, bny))
            elif (bnx, bny) in walls:
                return robot, boxes
            else:
                moving = False
        boxes = boxes.difference(move_boxes).union(new_boxes)

    return ((rnx, rny), boxes)


def print_map(robot, boxes, walls, w, h):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in walls:
                line += "#"
            elif (x, y) in boxes:
                line += "O"
            elif (x,y) == robot:
                line += "@"
            else:
                line += "."
        print(line)


for c in range(len(commands)):
    robot, boxes = move(commands[c], robot, boxes)
    #print(c, commands[c])
    #print_map(robot, boxes, walls, w, h)

gps = 0
for bx, by in boxes:
    #print(100*by, bx)
    gps += (100 * by + bx)

print(gps)