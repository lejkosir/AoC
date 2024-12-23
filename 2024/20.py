from collections import defaultdict
from heapq import heappush, heappop


def remake(filename):
    with open(filename) as file:
        d = defaultdict(str)
        for y, line in enumerate(file):
            for x , c in enumerate(line[:-1]):
                if c == "S":
                    start = (y,x)
                elif c == "E":
                    end = (y,x)
                d[(y,x)] = c
        return d, start, end


orients = [(0, 1),(1, 0),(0, -1),(-1, 0)]
exclude_values = {-1, 1}

orients1 = []
range1 = [i for i in range(-2, 3) if i not in exclude_values]
for i  in range1:
    for j in range1:
        if abs(i) + abs(j) != 4:
            orients1.append((i,j))

orients2 = []
range2 = [i for i in range(-20, 21)]
for i in range2:
    for j in range2:
        if abs(i) + abs(j) <= 20:
            orients2.append((i, j))

def first(filename):
    d, start, end = remake(filename)
    final = list(d.keys())[-1]
    basepath = pathfinder(d, start, end, final)
    end_cd = flood(d, end, final, defaultdict(int))
    start_cd = flood(d, start, final, defaultdict(int))
    c = 0
    for i in range(2):
        if i == 0:
            ori = orients1
        else:
            ori = orients2
        for key, value in start_cd.items():
            y, x = key
            for orient in ori:
                ny, nx = y + orient[0], x + orient[1]
                if (ny, nx) in end_cd and len(basepath) - (end_cd[ny, nx] + start_cd[y, x] + abs(orient[0]) + abs(orient[1])) > 100:
                    c += 1
        print(c)


def pathfinder(d, pos, end, final):
    l = [(0, pos, [pos])]
    visited = set()
    while True:
        cena, posi, path = heappop(l)
        if posi in visited:
            continue
        visited.add(posi)
        if posi == end:
            return path
        y, x = posi
        for o in orients:
            ny, nx = y + o[0], x + o[1]
            if 0 <= nx <= final[1] and 0 <= ny <= final[0]:
                if d[(ny,nx)] != "#":
                    np = path + [(ny,nx)]
                    heappush(l, (cena + 1, (ny, nx), np))


def flood(d, end, final, dcost):
    l = [(0, end, [end])]
    visited = set()
    try:
        while True:
            cena, posi, path = heappop(l)
            if posi in visited:
                continue
            visited.add(posi)
            dcost[posi] = len(path) - 1
            y, x = posi
            for o in orients:
                ny, nx = y + o[0], x + o[1]
                if 0 <= nx <= final[1] and 0 <= ny <= final[0]:
                    if d[(ny,nx)] != "#":
                        np = path + [(ny,nx)]
                        heappush(l, (cena + 1, (ny, nx), np))
    except IndexError:
        return dcost

first("files/20")
