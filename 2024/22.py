from collections import defaultdict

def remake(filename):
    with open(filename) as file:
        l = []
        for line in file:
            l.append(int(line[:-1]))
    return l

def first(filename):
    l = remake(filename)
    summed = 0
    for val in l:
        for i in range(2000):
            val = make(val)
        summed += val
    print(summed)

def second(filename):
    l = remake(filename)
    d = defaultdict(list)
    for val in l:
        key = val
        d[key].append(int(str(val)[-1]))
        for i in range(2000):
            val = make(val)
            d[key].append(int(str(val)[-1]))
    dchange = defaultdict(str)
    for key, value in d.items():
        for i, x in enumerate(value):
            if i == 0:
                dchange[key] += "+" + str(0)
            else:
                if value[i] - value[i-1] < 0:
                    dchange[key] += str(value[i] - value[i - 1])
                else:
                    dchange[key] += "+" + str(value[i] - value[i-1])

    max_bannanas = 0
    valids = []
    for fi in range(-9, 10):
        for se in range(-9, 10):
            if -9 > fi + se or 9 < fi + se:
                continue
            for th in range(-9, 10):
                if -9 > th + se or 10 < th + se or th + se + fi > 9 or th + se + fi < -9:
                    continue
                for fo in range(-9, 10):
                    if -9 > th + fo or 9 < th + fo:
                        continue
                    if fi + se + th + fo < -9 or fi + se + th + fo > 9:
                        continue
                    fis = str(fi) if fi < 0 else "+" + str(fi)
                    ses = str(se) if se < 0 else "+" + str(se)
                    fos = str(fo) if fo < 0 else "+" + str(fo)
                    ths = str(th) if th < 0 else "+" + str(th)
                    valids.append(fis + ses + ths + fos)


    for i, search in enumerate(valids):
        bannanas = 0
        for key, value in dchange.items():
            index = value.find(search)
            if index >= 0:
                index = index // 2 + 3
                bannanas += d[key][index]
        if bannanas > max_bannanas:
            max_bannanas = bannanas
    print(max_bannanas-5)


def make(val):
    val = ((val * 64) ^ val) % 16777216
    val = ((val // 32) ^ val) % 16777216
    val = ((val * 2048) ^ val) % 16777216
    return val

second("files/22")