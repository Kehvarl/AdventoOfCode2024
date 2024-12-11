from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()][0]
    # content = [int(x) for x in f.readlines()]

stones = defaultdict(int)

for s in content.split(" "):
    stones[int(s)] += 1


def step(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l = s[0:len(s)//2]
        r = s[len(s)//2:]
        return [int(l), int(r)]
    else:
        return[int(stone)*2024]


def fast_step(stones):
    new_stones = defaultdict(int)
    for s in stones:
        s_count = stones[s]
        for r in step(s):
            new_stones[r] += s_count
    return new_stones


for i in range(75):
    stones = fast_step(stones)

sum = 0
for s in stones:
    sum += stones[s]
print(sum)