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

secrets = []
for s in content:
    ns = s
    for i in range(2000):
        ns = next_secret(ns)
        if s == 1 and ns == 8685429:
            print(i)
    secrets.append(ns)
print(secrets)
print(sum(secrets))