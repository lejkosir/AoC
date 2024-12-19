from collections import defaultdict

def remake(filename):
    with open(filename) as file:
        d_all = defaultdict(str)
        moves = []
        ct = 0
        for i, line in enumerate(file):
            if line == "\n":
                ct += 1
            if not ct:
                for j, x in enumerate(line[:-1]):
                    if x == "@":
                        curr = (i,j)
                    d_all[(i, j)] = x
            else:
                for x in line[:-1]:
                    moves.append(x)
    return d_all, moves, curr


def pt2remake(filename):
    with open(filename) as file:
        d_all = defaultdict(str)
        moves = []
        ct = 0
        for i, line in enumerate(file):
            jct = 0
            if line == "\n":
                ct += 1
            if not ct:
                for j, x in enumerate(line[:-1]):
                    if x == "@":
                        curr = (i,j+jct)
                        d_all[(i, j + jct)] = x
                        jct += 1
                        d_all[(i, j + jct)] = "."
                    elif x == "O":
                        d_all[(i, j + jct)] = "["
                        jct += 1
                        d_all[(i, j + jct)] = "]"
                    else:
                        d_all[(i, j + jct)] = x
                        jct += 1
                        d_all[(i, j + jct)] = x
            else:
                for x in line[:-1]:
                    moves.append(x)
    return d_all, moves, curr


trans = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def second(filename, num):
    d, moves, curr = pt2remake(filename)
    print(d)
    summed = 0
    for move in moves:
        involved = set()
        if algo(d, move, curr, 0, involved):
            curr = mover(d, curr, involved, move)
    for key, value in d.items():
        if value == "[":
            summed += key[0] * 100 + key[1]
    print(summed)
    
    d, moves, curr = remake(filename)
    summed = 0
    for move in moves:
        involved = set()
        if checker(d, move, curr, involved):
            curr = mover(d, curr, involved, move)
    for key, value in d.items():
        if value == "O":
            summed += key[0] * 100 + key[1]
    print(summed)


def mover(d, curr, involved, move):
    xd = [x for x in involved]
    match move:
        case "^":
            xd = sorted(xd, key=lambda x: x[0])
            for y, x in xd:
                ny, nx = y + trans[0][0], x + trans[0][1]
                d[ny, nx] = d[y, x]
                d[y, x] = "."
            curr = curr[0] - 1, curr[1]
        case ">":
            xd = sorted(xd, key=lambda x: x[1], reverse=True)
            for y, x in xd:
                ny, nx = y + trans[1][0], x + trans[1][1]
                d[ny, nx] = d[y, x]
                d[y, x] = "."
            curr = curr[0], curr[1] + 1
        case "v":
            xd = sorted(xd, key=lambda x: x[0], reverse=True)
            for y, x in xd:
                ny, nx = y + trans[2][0], x + trans[2][1]
                d[ny, nx] = d[y, x]
                d[y, x] = "."
            curr = curr[0] + 1, curr[1]
        case "<":
            xd = sorted(xd, key=lambda x: x[1])
            for y, x in xd:
                ny, nx = y + trans[3][0], x + trans[3][1]
                d[ny, nx] = d[y, x]
                d[y, x] = "."
            curr = curr[0], curr[1] - 1
    return curr

def checker(d, move, pos, inv):
    match move:
        case "^":
            if d[pos] == "@":
                if algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == "O":
                if algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == ".":
                return 1

        case ">":
            if d[pos] == "@":
                if algo(d, move, (pos[0], pos[1] + 1), 0, inv):
                    return 1
            elif d[pos] == "O":
                if algo(d, move, (pos[0], pos[1] + 1), 0, inv):
                    return 1
            elif d[pos] == ".":
                return 1

        case "v":
            if d[pos] == "@":
                if algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == "O":
                if algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == ".":
                return 1

        case "<":
            if d[pos] == "@":
                if algo(d, move, (pos[0], pos[1]- 1), 0, inv):
                    return 1
            elif d[pos] == "O":
                if algo(d, move, (pos[0], pos[1]- 1), 0, inv):
                    return 1
            elif d[pos] == ".":
                return 1
    return 0


def algo(d, move, pos, flag, inv):
    if d[pos] != "." and d[pos] != "#":
        inv.add(pos)
    match move:
        case "^":
            if d[pos] == "@":
                if algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == "[":
                if flag:
                    if algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                        return 1
                else:
                    if algo(d, move, (pos[0], pos[1] + 1), 1, inv) and algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                        return 1
            elif d[pos] == "]":
                if flag:
                    if algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                        return 1
                else:
                    if algo(d, move, (pos[0], pos[1] - 1), 1, inv) and algo(d, move, (pos[0] - 1, pos[1]), 0, inv):
                        return 1
            elif d[pos] == ".":
                return 1
            else:
                return 0
        case ">":
            if d[pos] != "#" and d[pos] != ".":
                if algo(d, move, (pos[0], pos[1] + 1), 0, inv):
                    return 1
            if d[pos] == ".":
                return 1

        case "v":
            if d[pos] == "@":
                if algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                    return 1
            elif d[pos] == "[":
                if flag:
                    if algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                        return 1
                else:
                    if algo(d, move, (pos[0], pos[1] + 1), 1, inv) and algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                        return 1
            elif d[pos] == "]":
                if flag:
                    if algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                        return 1
                else:
                    if algo(d, move, (pos[0], pos[1] - 1), 1, inv) and algo(d, move, (pos[0] + 1, pos[1]), 0, inv):
                        return 1
            elif d[pos] == ".":
                return 1
            return 0
        case "<":
            if d[pos] != "#" and d[pos] != ".":
                if algo(d, move, (pos[0], pos[1] - 1), 0, inv):
                    return 1
            if d[pos] == ".":
                return 1


second("files/test1", 1)

