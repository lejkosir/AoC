# ce dela, dela
def remake(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            nl = []
            for x in line[:-1]:
                nl.append(x)
            lines.append(nl)
        return lines

def first(filename):
    lines = remake(filename)
    xmases = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            l = [0,0,0,0,0,0,0,0]
            if c == "X":
                print(y,x)
                # res bi lahk fix bolse napisal.
                for i in range(1, 4):
                    # >
                    try:
                        if l[0] == 0 and lines[y][x+i] == "M" or l[0] == 1 and lines[y][x+i] == "A" or l[0] == 2 and lines[y][x+i] == "S":
                            l[0] += 1
                    except:
                        pass
                    #v>
                    try:
                        if l[1] == 0 and lines[y+i][x + i] == "M" or l[1] == 1 and lines[y+i][x + i] == "A" or l[1] == 2 and lines[y+i][x + i] == "S":
                            l[1] += 1
                    except:
                        pass
                    #v
                    try:
                        if l[2] == 0 and lines[y + i][x] == "M" or l[2] == 1 and lines[y + i][x] == "A" or l[2] == 2 and lines[y + i][x] == "S":
                            l[2] += 1
                    except:
                        pass
                    #<v
                    try:
                        if x - i < 0:
                            pass
                        elif l[3] == 0 and lines[y + i][x-i] == "M" or l[3] == 1 and lines[y + i][x-i] == "A" or l[3] == 2 and \
                                lines[y + i][x-i] == "S":
                            l[3] += 1
                    except:
                        pass
                    #<
                    try:
                        if x - i < 0:
                            pass
                        elif l[4] == 0 and lines[y][x - i] == "M" or l[4] == 1 and lines[y][x - i] == "A" or l[
                            4] == 2 and lines[y][x - i] == "S":
                            l[4] += 1
                    except:
                        pass
                    #</\
                    try:
                        if y-i < 0 or x - i < 0:
                            pass
                        elif l[5] == 0 and lines[y-i][x - i] == "M" or l[5] == 1 and lines[y-i][x - i] == "A" or l[
                            5] == 2 and lines[y-i][x - i] == "S":
                            l[5] += 1
                    except:
                        pass
                    #/\
                    try:
                        if y-i < 0:
                            pass
                        elif l[6] == 0 and lines[y - i][x] == "M" or l[6] == 1 and lines[y - i][x] == "A" or l[
                            6] == 2 and lines[y - i][x] == "S":
                            l[6] += 1
                    except:
                        pass
                    #/\>
                    try:
                        if y-i < 0:
                            pass
                        elif l[7] == 0 and lines[y - i][x+i] == "M" or l[7] == 1 and lines[y - i][x+i] == "A" or l[
                            7] == 2 and lines[y - i][x+i] == "S":
                            l[7] += 1
                    except:
                        pass
                print(l)
                for n in l:
                    if n == 3:
                        xmases += 1
            else:
                pass
    print(xmases)


def second(filename):
    lines = remake(filename)
    xmases = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "A":
                try:
                    # M.S
                    # .A.
                    # M.S
                    if lines[y-1][x-1] == "M" and  lines[y+1][x-1] == "M" and lines[y-1][x+1] == "S" and  lines[y+1][x+1] == "S" and y-1 >= 0 and x >= 0:
                        xmases += 1
                    # S.M
                    # .A.
                    # S.M
                    elif lines[y-1][x-1] == "S" and  lines[y+1][x-1] == "S" and lines[y-1][x+1] == "M" and  lines[y+1][x+1] == "M" and y-1 >= 0 and x >= 0:
                        xmases += 1
                    # M.M
                    # .A.
                    # S.S
                    elif lines[y-1][x-1] == "M" and  lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S" and  lines[y+1][x+1] == "S" and y-1 >= 0 and x >= 0:
                        xmases += 1
                    # S.S
                    # .A.
                    # M.M
                    elif lines[y-1][x-1] == "S" and  lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M" and  lines[y+1][x+1] == "M" and y-1 >= 0 and x >= 0:
                        xmases += 1
                except:
                    pass
    print(xmases)
second("files/4")