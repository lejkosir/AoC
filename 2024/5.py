def remake(filename):
    with open(filename) as file:
        rules = {}
        prints = []
        f = True
        for line in file:
            if line == "\n":
                f = False
            elif f:
                ln = line[:-1].split("|")
                if int(ln[0]) not in rules:
                    rules[int(ln[0])] = [int(ln[1])]
                else:
                    rules[int(ln[0])].append(int(ln[1]))
            else:
                l = []
                for x in line[:-1].split(","):
                    l.append(int(x))
                prints.append(l)
    return rules, prints


def first(filename):
    rules, prints = remake(filename)
    wrong_order = []
    summed = 0
    for pr in prints:
        printable = True
        for i, p in enumerate(pr):
            if p in rules and printable:
                for rule in rules[p]:
                    if rule in pr[:i]:
                        printable = False
                        wrong_order.append(pr)
                        break
        if printable:
            summed += pr[int((len(pr) - 1) / 2)]
    print(summed)
    return wrong_order


def second(filename):
    rules, prints = remake(filename)
    wrong = first(filename)
    summed = 0
    for prin in wrong:
        fixed = check(rules, prin)
        summed +=  fixed[int((len(fixed) - 1) / 2)]
    print(summed)

# rekurzija 
def check(rules, prin):
    neu = prin.copy()
    flag = True
    for i, p in enumerate(prin):
        f = -1
        if p in rules:
            for rule in rules[p]:
                if rule in prin[:i]:
                    flag = False
                    f = prin[:i].index(rule)
                    break
            if f >= 0:
                neu.remove(p)
                neu.insert(f, p)
                break
    if flag:
        return neu
    else:
        return check(rules, neu)


second("files/5")
