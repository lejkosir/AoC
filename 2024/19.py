def remake(filename):
    with open(filename) as file:
        combos = []
        for i, line in enumerate(file):
            if i == 0:
                towels = line[:-1].split(", ")
            if i > 1:
                combos.append(line[:-1])
        return towels, combos

def second(filename):
    t, c = remake(filename)
    count1 = 0
    count2 = 0
    cache = {}
    for i, com in enumerate(c):
        xd = dfs2(com, t, cache)
        if xd:
            count1 += 1
            count2 += xd
    print(count1)
    print(count2)


def dfs2(combo, towels, cache):
    if combo in cache:
        return cache[combo]

    if combo == "":
        return 1

    ways = 0
    for t in towels:
        if combo.startswith(t):
            ways += dfs2(combo[len(t):], towels, cache)
    cache[combo] = ways
    return ways



second("files/19")