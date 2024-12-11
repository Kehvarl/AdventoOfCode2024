from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()][0]
    # content = [int(x) for x in f.readlines()]

stones = [int(x) for x in content.split(" ")]


def step(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            l = s[0:len(s)//2]
            r = s[len(s)//2:]
            new_stones.append(int(l))
            new_stones.append(int(r))
        else:
            new_stones.append((stone * 2024))
    return new_stones

print(stones)
for i in range(25):
    stones = step(stones)
    print(stones)
print(len(stones))