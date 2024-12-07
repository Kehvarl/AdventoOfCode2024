from collections import defaultdict, deque
from pprint import pprint
from itertools import product

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

solve = []
for calc in content:
    total, rest = calc.split(": ")
    total = int(total)
    vals = [int(x) for x in rest.split(" ")]
    solve.append((total, vals))


def test(vals, ops):
    result = vals[0]
    for i, o in enumerate(ops):
        if o == "+":
            result += vals[i + 1]
        elif o == "*":
            result *= vals[i + 1]
        elif o == "||":
            result = int(str(result) + str(vals[i + 1]))
    return result

result = 0
for s in solve:
    total, vals = s
    ops = len(vals) - 1
    combinations = product(["+", "*", "||"], repeat=ops)

    valid = False
    for c in combinations:
        if test(vals, c) == total:
            valid = True
            break
    if valid:
        result += total

print(result)


