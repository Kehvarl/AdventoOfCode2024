from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [int(x.strip()) for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


def next_secret(secret):
    ns = ((secret * 64) ^ secret) % 16777216
    ns = ((ns // 32) ^ ns) % 16777216
    ns = ((ns * 2048) ^ ns) % 16777216
    return ns


buyers = {}
for s in content:
    states = [(int(str(s)[-1]), None)]
    changes = []
    ns = s
    for i in range(2000):
        ns = next_secret(ns)
        price = int(str(ns)[-1])
        changes.append(price - states[-1][0])
        states.append((price, price - states[-1][0]))
    buyers[s] = (states, changes)

bests = []
for b in buyers:
    states, changes = buyers[b]
    best = 0
    best_i = []
    pattern = []
    for i, s in enumerate(states):
        p, c = s
        if p > best:
            best = p
            best_i = [i+1]
        elif p == best:
            best_i.append(i+1)
        if c == 3 and pattern[-1] == -1 and pattern[-2] == 1 and pattern[-3] == -2:
            pass #print(i, p, s, best, best_i[-1])
        pattern.append(c)
    bests.append((best, pattern, best_i))


tests = []
for b in bests:
    b, p, i = b
    for ii in i:
        patt = p[ii - 4: ii]
        if patt:
            tests.append(patt)


best = 0
best_p = []
for t in tests:
    price = 0
    for b in buyers:
        states, changes = buyers[b]
        for i, s in enumerate(changes[:-4]):
            if changes[i:i+4] == t:
                price += states[i + 4][0]
                break
    if price > best:
        best = price
        best_p = t

print(best, best_p)


