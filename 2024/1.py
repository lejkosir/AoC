def refactor(filename):
    leftlist, rightlist = [], []
    for line in open(filename):
        l, r = line.split("   ")
        leftlist.append(int(l))
        rightlist.append(int(r[:-1]))

    return sorted(leftlist), sorted(rightlist)

def first(filename):
    diff = 0
    leftlist, rightlist = refactor(filename)
    for x in zip(leftlist, rightlist):
        diff += abs(x[0] - x[1])
    print(diff)

def second(filename):
    simfac = 0
    leftlist, rightlist = refactor(filename)
    for l in leftlist:
        num = rightlist.count(l)
        simfac += num * l
    print(simfac)

first("files/1")
second("files/1")


