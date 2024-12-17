

match = [2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0]
# match = [0,3,5,4,3,0]
running = True
A = 33940147
lm = 0
while running:
    orig = A
    out = []
    while A > 0:
        out.append((((A % 8) ^ 5) ^ 6) ^ (A // (2 ** ((A % 8) ^ 5))) % 8)
        # out.append((A // 8) % 8)
        A = A // 8
    if out == match:
        print(orig)
        break
    if len(out) == len(match):
        if lm == 0:
            print("length match", orig, lm, (orig - lm))
        lm = orig
    if out[:6] == match[:6]:
        print("prefix", orig)
    if lm == 0:
        A = orig * 2
    else:
        A = orig + 2097152


