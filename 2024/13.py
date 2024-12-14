from heapq import heappop, heappush
from sympy import symbols, Eq, solve

def remake(filename):
    with open(filename) as file:
        xd = file.read()
        c = 0
        added = 10000000000000
        l = [[] for i in range(len(xd.split('\n'))//4)]
        l2 = [[] for i in range(len(xd.split('\n'))//4)]
        mc = 0
        for i, x in enumerate(xd.split('\n')):
            if c == 0 or c == 1:
                a = x.split(' ')
                l[mc].append((int(a[2][2:-1]), int(a[3][2:])))
                l2[mc].append((int(a[2][2:-1]), int(a[3][2:])))
                c += 1
            elif c == 2:
                a = x.split(' ')
                l[mc].append((int(a[1][2:-1]), int(a[2][2:])))
                l2[mc].append((added + int( a[1][2:-1]), added +int(a[2][2:])))
                c += 1
            else:
                c = 0
                mc += 1
    return l, l2

def first(filename):
    summed = 0
    l, l2 = remake(filename)
    for line in l:
        summed += sistem(line)
    print(summed)
    summed = 0
    for line in l2:
         summed += sistem(line)
    print(summed)


# mislil da sem pameten z bfs s cenami ampak neuporabno za p2
def algo(line):
    ax, ay = line[0]
    bx, by = line[1]
    tx, ty = line[2]
    pque = [(0, 0, 0)] # cena, cilj x, cilj y
    visited = set()
    while pque:
        cena, x, y = heappop(pque)

        if (x, y) == (tx, ty):
            return cena
        if (x, y) in visited:
            continue
        visited.add((x, y))
        # a
        nx, ny = ax + x, ay + y
        if nx <= tx and ny <= ty:
            heappush(pque, (cena + 3, nx , ny))

        nx, ny = bx + x, by + y
        if nx <= tx and ny <= ty:
            heappush(pque, (cena + 1, nx , ny))
    return 0

# racunanje sistema enacb
def sistem(line):
    ax, ay = line[0]
    bx, by = line[1]
    tx, ty = line[2]

    x, y = symbols("x y")
    enx = Eq(ax*x + bx*y, tx)
    eny = Eq(ay*x + by*y, ty)
    res = solve((enx, eny), (x, y))
    x, y = res[x], res[y]
    if x.is_integer and y.is_integer:
        return x * 3 + y
    else:
        return 0


first("files/13")