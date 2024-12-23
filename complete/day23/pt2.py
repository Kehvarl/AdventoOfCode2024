from collections import defaultdict, deque
from pprint import pprint
import networkx as nx


with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


graph = nx.Graph()
for y, v1 in enumerate(content):
    a, b = v1.split("-")
    graph.add_edge(a, b)

cliques = [c for c in nx.find_cliques(graph)]
longest = []
for c in cliques:
    if len(c) > len(longest):
        longest = c
print(",".join(sorted(longest)))


