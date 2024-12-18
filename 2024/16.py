from collections import defaultdict
from heapq import heappop, heappush

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


orients = [(0,1), (1,0), (0,-1), (-1,0)]

def first(filename):
    d, start, end = remake(filename)
    ori = (0, 1)
    visited = set()
    xd = algo(start, end, d, ori)
    for x in xd:
        for xx in x:
            visited.add(xx)

    print(len(visited))



def algo(start, end, d, ori):
    l = [(0, start, ori, [start])]
    visited = {}
    ends = []
    mincost = 0

    while l:
        cena, pos, orien, path = heappop(l)
        if (pos, orien) in visited and visited[(pos, orien)] < cena:
            continue
        visited[(pos, orien)] = cena

        if pos == end:
            if mincost == 0:
                mincost = cena
            if cena == mincost:
                ends.append(path)

        for orient in orients:
            ny, nx = pos[0] + orient[0], pos[1] + orient[1]
            if d.get((ny, nx), '#') != '#':
                cost = cena + 1
                if orien != orient:
                    cost += 1000

                new_path = path + [(ny, nx)]

                if (ny, nx) not in visited or cost <= visited.get((ny, nx), float('inf')):
                    heappush(l, (cost, (ny, nx), orient, new_path))

    return ends

first("files/16")