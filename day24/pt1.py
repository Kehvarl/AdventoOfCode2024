from collections import defaultdict, deque
from pprint import pprint
from queue import Queue

with open("input.txt") as f:
    values, connections = f.read().strip().split("\n\n")
    # content = [int(x) for x in f.readlines()]

wires = {}

for v in values.split("\n"):
    w, val = v.split(": ")
    wires[w] = int(val)

gates = {}
zmax= 0
for c in connections.split("\n"):
    i, o = c.split(" -> ")
    o = o.strip()
    if o[0] == 'z':
        zmax = max([zmax, int(o[1:])])
    if "AND" in i:
        gate = "AND"
    elif "XOR" in i:
        gate = "XOR"
    elif "OR" in i:
        gate = "OR"
    a, b = i.split(gate)
    gates[o] = (gate, a.strip(), b.strip())

inputs = {}
zs = [0 for _ in range(zmax+1)]
q = deque(gates.keys())
while q:
    out = q.popleft()

    gate, a, b = gates[out]

    if a not in wires or b not in wires:
        q.append(out)
        continue

    if gate == "AND":
        wires[out] = wires[a] & wires[b]
    elif gate == "XOR":
        wires[out] = wires[a] ^ wires[b]
    elif gate == "OR":
        wires[out] = wires[a] | wires[b]
    else:
        print("invalid gate ", gate)
        break

    if out[0] == 'z':
        zs[int(out[1:])] = wires[out]


print("".join([str(s) for s in reversed(zs)]))

print(int("".join([str(s) for s in reversed(zs)]), 2))

