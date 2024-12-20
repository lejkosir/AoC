from heapq import heappop, heappush
from collections import defaultdict


def remake(filename):
    with open(filename) as file:
        d = defaultdict(int)
        for line in file:
            x, y = line[:-1].split(',')
            d[(x,y)] = 1

def first(filename):
    pos = (0,0)
    end = (70,70)
    with open(filename) as file:
        d = defaultdict(int)
        for i in range(pos[0], end[0] + 1):
            for j in range(pos[1], end[1] + 1):
                d[(i,j)] = 0
        for i, line in enumerate(file):
            if i == 1024:
                break
            x, y = line[:-1].split(',')
            d[(int(x),int(y))] = 1
        print(len(pathfinder(d, pos, end)[1:]))

def second(filename):
    pos = (0,0)
    end = (70,70)
    with open(filename) as file:
        d = defaultdict(int)
        for i in range(pos[0], end[0] + 1):
            for j in range(pos[1], end[1] + 1):
                d[(i,j)] = 0
        for i, line in enumerate(file):
            x, y = line[:-1].split(',')
            d[(int(x), int(y))] = 1
            try:
                pathfinder(d, pos, end)
            except:
                print(x, y)
                break


orients = [(1,0),(0,1),(-1, 0),(0,-1)]

def pathfinder(d, pos, end):
    l = [(0, pos, [pos])]
    visited = set()
    while True:
        cena, posi, path = heappop(l)
        if posi in visited:
            continue
        visited.add(posi)
        if posi == end:
            return path
        x, y = posi
        for o in orients:
            nx, ny = x + o[0], y + o[1]
            if 0 <= nx <= end[0] and 0 <= ny <= end[1]:
                if d[(nx,ny)] != 1:
                    np = path + [(nx,ny)]
                    heappush(l, (cena + 1, (nx, ny), np))


first("files/18")
second("files/18")