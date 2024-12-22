from collections import defaultdict, deque
from pprint import pprint
from queue import Queue

with open("test.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

keypad1 = {
    "9": (2, 0),
    "8": (1, 0),
    "7": (0, 0),
    "6": (2, 1),
    "5": (1, 1),
    "4": (0, 1),
    "3": (2, 2),
    "2": (1, 2),
    "1": (0, 2),
    "A": (2, 3),
    "0": (1, 3)
}
reverse_keypad1 = {
    (2, 0): "9",
    (1, 0): "8",
    (0, 0): "7",
    (2, 1): "6",
    (1, 1): "5",
    (0, 1): "4",
    (2, 2): "3",
    (1, 2): "2",
    (0, 2): "1",
    (2, 3): "A",
    (1, 3): "0"
}

directionmap = {
    (-1, 0): "<",
    (1, 0): ">",
    (0, -1): "^",
    (0, 1): "v"
}

keypad2 = {
    "A": (2, 0),
    "^": (1, 0),
    ">": (2, 1),
    "v": (1, 1),
    "<": (0, 1),
}

reverse_keypad2 = {
    (2, 0): "A",
    (1, 0): "^",
    (2, 1): ">",
    (1, 1): "v",
    (0, 1): "<"
}


def bfs(start, end, w, h, exclude):
    bfs_q = Queue()
    bfs_q.put((start, [(start)], []))
    visited = set()
    visited.add(start)

    while not bfs_q.empty():
        pos, path, buttons = bfs_q.get()
        x, y, = pos

        if (x, y) == end:
            return path, buttons
        if buttons == []:
            neighbors = [(0, 1, "v"), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]
        else:
            neighbors = [buttons[-1], (0, 1, "v"), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]

        for dx, dy, d in neighbors:
            tx, ty = x + dx, y + dy
            if (0 <= ty < h and 0 <= tx < w) and ((tx, ty) not in path) and (tx, ty) not in exclude:
                bfs_q.put(((tx, ty), path + [(tx, ty)], buttons +[(dx, dy, d)]))
                visited.add((tx, ty))
    return None


robot1pos = (2, 3)
r1x, r1y = robot1pos
robot2pos = (2, 0)
r2x, r2y = robot2pos
robot2pos = (2, 0)
r2x, r2y = robot2pos
robot3pos = (2, 0)
r3x, r3y = robot2pos
total = 0

for code in ["379A"]:
    print(code)
    moves = []
    moves2 = []
    moves3 = []
    outcode = ""
    outcode2 = ""
    outcode3 = ""
    for char in code:
        cx, cy = keypad1[char]
        if (r1x, r1y) != (cx, cy):
            path, buttons = bfs((r1x, r1y), (cx, cy), 3, 4, [(0, 3)])
            #print(char, cx, cy, path)
            for b in buttons:
                moves.append(b[2])
            (r1x, r1y) = (cx, cy)
        moves.append("A")
        outcode += reverse_keypad1[(r1x, r1y)]
    for move in moves:
        mx, my = keypad2[move]
        if (r2x, r2y) != (mx, my):
            path, buttons = bfs((r2x, r2y), (mx, my), 3, 2, [(0, 0)])
            #print(char, move, (r2x, r2y), (mx, my), buttons)
            for b in buttons:
                moves2.append(b[2])
            (r2x, r2y) = (mx, my)
        moves2.append("A")
        outcode2 += reverse_keypad2[(r2x, r2y)]
    for move2 in moves2:
        m2x, m2y = keypad2[move2]
        #print(move2, (r3x, r3y), (m2x, m2y))
        if (r3x, r3y) != (m2x, m2y):
            path, buttons = bfs((r3x, r3y), (m2x, m2y), 3, 2, [(0, 0)])
            #print(move2, (r3x, r3y), (m2x, m2y), path)
            for b in buttons:
                moves3.append(b[2])
            (r3x, r3y) = (m2x, m2y)
        moves3.append("A")
        #print(move2, "A")
        outcode3 += reverse_keypad2[(r3x, r3y)]

    total += len(moves2) * int(code.strip("A"))

    #print(moves)
    #print(len(moves))
    print(outcode)
    #print(moves2)
    #print(len(moves2))
    print(outcode2)
    #print("".join(moves))
    print(moves3)
    print(len(moves3))
    print(outcode3)
    #print("".join(moves2))
    print("".join(moves3))
print(total)