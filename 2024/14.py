from collections import defaultdict

def remake(filename):
    with open(filename) as file:
        d = defaultdict(list)
        for i, line in enumerate(file):
            xxx = line[:-1].split(" ")
            pv = xxx[0][2:].split(",") + xxx[1][2:].split(",")
            pvint = [int(x) for x in pv]
            d[i] = pvint
    return d

# trial and error, nekako danger najmanjsi ko je na sliki drevo?
def first(filename, xlim, ylim):
    d = remake(filename)
    lowesti = 0
    lowestd = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    xd = (xlim // 2, ylim // 2)
    quads = [(0, 0, xd[0] - 1, xd[1] - 1), (xd[0] + 1, 0, 2 * xd[0], xd[1] - 1), (0, xd[1] + 1, xd[0] - 1, xd[1] * 2),
             (xd[0] + 1, xd[1] + 1, xd[0] * 2, xd[1] * 2)]
    for i in range(10000):
        for key, value in d.items():
            nval = [(value[0] + value[2]) % xlim, (value[1] + value[3]) % ylim, value[2], value[3]]
            d[key] = nval
        qd = [0, 0, 0, 0]

        for key, val in d.items():
            x, y = val[0], val[1]
            for j, quad in enumerate(quads):
                if quad[0] <= x <= quad[2] and quad[1] <= y <= quad[3]:
                    qd[j] += 1
        summed = 1
        for q in qd:
            summed *= q
        if summed < lowestd:
            lowestd = summed
            lowesti = i
        print(summed, i)
    print(lowesti + 1)


first("files/14", 101, 103)