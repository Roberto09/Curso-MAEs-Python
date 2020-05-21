a = open('tarch.txt', 'r')

mis_coord = []

for ln in a:
    ln = ln[:-1]
    a, b = ln.split(' ')
    a = float(a)
    b = float(b)
    mis_coord.append((a, b))

mis_coord.reverse()

for crd in mis_coord:
    print(crd)