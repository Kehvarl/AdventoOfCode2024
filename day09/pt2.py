from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()][0]
    # content = [int(x) for x in f.readlines()]

files = []
file_ids = {}
empty = []

file = True
fi = 0
for y, v1 in enumerate(content):
    if file:
        file_ids[fi] = int(v1)
        files.extend([fi]*int(v1))
        file = False
    else:
        empty.append((len(files), int(v1)))
        files.extend(['.']*int(v1))
        file = True
        fi += 1

idx = len(files) - 1
while idx >= 0:
    if files[idx] != '.':
        file_len = file_ids[files[idx]]
        empty_index = None
        for ei, e in enumerate(empty):
            if e[1] >= file_len and e[0] < idx:
                empty_index = ei
                break
        if empty_index is not None:
            i, s = empty.pop(empty_index)
            for f in range(file_len):
                files[i] = files[idx - f]
                files[idx - f] = '.'
                i += 1
            if file_len < s:
                empty.insert(empty_index, (i, s-file_len))
        idx -= file_len
    else:
        idx -= 1

# print(files)
cs = 0
for y, v1 in enumerate(files):
    if v1 != '.':
        cs += (y * int(v1))
print(cs)