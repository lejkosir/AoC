import re
def main(filename):
    with open(filename) as f:
        summed = 0
        l = []
        regex =re.compile(r"mul\(\b[0-9]{1,3}\b,\b[0-9]{1,3}\b\)|do\(\)|don't\(\)")
        for line in f:
            all = re.findall(regex,line)
            print(all)
            for i in all:
                if i == "don't()" or i == "do()":
                    l.append (i)
                else:
                    x = i.split(',')
                    l.append((int(x[0][4:]),int(x[1][:-1])))

        flag = 1
        for i in l:
            if i == "do()":
                flag = 1
            elif i == "don't()":
                flag = 0
            else:
                if flag == 1:
                    summed += i[0] * i[1]
                else:
                    pass
        print(summed)
main("files/3")