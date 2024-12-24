from collections import defaultdict, deque
from pprint import pprint
from queue import Queue
import networkx as nx

with open("input.txt") as f:
    values, connections = f.read().strip().split("\n\n")
    # content = [int(x) for x in f.readlines()]

wires = {}

ymax = 1
xmax = 1
for v in values.split("\n"):
    w, val = v.split(": ")
    wires[w] = int(val)
    if w[0] == 'x':
        xmax = max([xmax, int(w[1:])])
    elif w[0] == 'y':
        ymax = max([ymax, int(w[1:])])

xs = [0 for _ in range(xmax+1)]
ys = [0 for _ in range(ymax+1)]
for w in wires:
    if w[0] == 'x':
        xs[int(w[1:])] = wires[w]
    elif w[0] == 'y':
        ys[int(w[1:])] = wires[w]

gates = {}
graph = nx.Graph()
zmax= 1
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
    a, b = a.strip(), b.strip()
    gates[o] = (gate, a, b)
    graph.add_edge(o, a)
    graph.add_edge(o, b)


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
    elif out[0] == 'x':
        xs[int(out[1:])] = wires[out]
    elif out[0] == 'y':
        ys[int(out[1:])] = wires[out]


print("".join([str(s) for s in reversed(xs)]))
print("".join([str(s) for s in reversed(ys)]))
print("".join([str(s) for s in reversed(zs)]))

print((int("".join([str(s) for s in reversed(xs)]), 2) + int("".join([str(s) for s in reversed(ys)]), 2)))
print((int("".join([str(s) for s in reversed(zs)]), 2)))


