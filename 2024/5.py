import random

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
    print(rules)
    return rules, prints


def first(filename):
    rules, prints = remake(filename)
    prints2 = []
    summed = 0
    for pr in prints:

        printable = True
        for i, p in enumerate(pr):
            if p in rules and printable:
                for rule in rules[p]:
                    if rule in pr[:i]:
                        printable = False
                        prints2.append(pr)
                        break
        if printable:
            print("scoooooooooooooooooooore")
            summed += pr[int((len(pr) - 1) / 2)]
    print(summed)

    return rules, prints2




first("files/5")