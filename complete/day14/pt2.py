from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


robots = []
for r in content:
    p, v = r.split(" ")
    px = int(p.split(",")[0][2:])
    py = int(p.split(",")[1])
    vx = int(v.split(",")[0][2:])
    vy = int(v.split(",")[1])
    robots.append((px, py, vx, vy))


def turn(robots, w, h):
    new_robots = []
    for px, py, vx, vy in robots:
        nx = (px + vx) % w
        ny = (py + vy) % h
        new_robots.append((nx, ny, vx, vy))
    return new_robots


def print_robots(robots, w, h):
    for y in range(h):
        line = ""
        for x in range(w):
            c = 0
            for r in robots:
                if (r[0], r[1]) == (x, y):
                    c += 1
            if c > 0:
                line += str(c)
            else:
                line += "."
        print(line)

def get_quadrants(robots, w, h):
    quadrants = [0,0,0,0]

    for rx, ry, _, _ in robots:
        q = None
        if ry < (h // 2):
            if rx < (w // 2):
                q = 0
            elif rx > (w // 2):
                q = 1
        elif ry > (h // 2):
            if rx < (w // 2):
                q = 2
            elif rx > (w // 2):
                q = 3

        if q is not None:
            print(rx, ry, q)
            quadrants[q] += 1

    return quadrants


def robot_positions(robots):
    positions = []
    for rx, ry, _, _ in robots:
        positions.append((rx, ry))
    return positions


def get_blob(robots, w, h):
    nearby = 0
    robot_set = set(robot_positions(robots))
    for y in range(h):
        for x in range(w):
            if (x, y) in robot_set and (x + 1, y) in robot_set:
                nearby += 1
    return nearby

w = 101
h = 103
has_tree = False
for i in range(10000):
    robots = turn(robots, w, h)
    blob = get_blob(robots, w, h)
    if blob > 100:
        print(blob)
        print_robots(robots, w, h)
        print(i + 1)

