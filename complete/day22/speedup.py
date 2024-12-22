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
    prices = [int(str(s)[-1])]
    changes = []
    ns = s
    for i in range(2000):
        ns = next_secret(ns)
        price = int(str(ns)[-1])
        changes.append(price - states[-1][0])
        prices.append(price)
        states.append((price, price - states[-1][0]))
    buyers[s] = (changes, prices)

pricemaps = defaultdict(int)
Count = 0
for b in buyers:
    changes, prices = buyers[b]
    tested = set()
    for i, s in enumerate(changes[:-4]):
        test = tuple(changes[i:i+4])
        price = prices[i + 4]
        if test in tested:
            continue
        tested.add(test)
        pricemaps[test] += price
best = 0
for p in pricemaps:
    best = max([best, pricemaps[p]])
print(best)
