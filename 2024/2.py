def remake(filename):
    with open(filename) as file:
        numint = []
        for line in file:
            n = []
            nums = line.split(' ')
            for num in nums:
                n.append(int(num))
            numint.append(n)
    return numint


def main(filename):
    nums = remake(filename)
    summed = 0
    for num in nums:
        asc = 0
        for x in zip(num, num[1:]):
            if x[1] - x[0] > 0:
                asc += 1
            else:
                asc -= 1
        summed += funct(num, asc)
    print(summed)

# neucinkovit bruteforce
def funct(num, asc):
    for i, x in enumerate(num):
        if i == 0:
            add = 1
            for y in zip(num, num[1:]):
                if asc > 0:
                    if not 1 <= y[1] - y[0] <= 3:
                        add = 0
                else:
                    if not 1 <= y[0] - y[1] <= 3:
                        add = 0
            if add != 0:
                return add
        add = 1
        xd = num.copy()
        xd.pop(i)
        for y in zip(xd, xd[1:]):
            if asc > 0:
                if not 1 <= y[1] - y[0] <= 3:
                    add = 0
            else:
                if not 1 <= y[0] - y[1]<= 3:
                    add = 0
        if add:
            return add
    return 0


main("files/2")