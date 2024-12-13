from collections import defaultdict

def main(filename, blinks):
    xd = defaultdict(int)
    summed = 0
    with open(filename) as file:
        for line in file:
            for c in line.split(" "):
                xd[int(c)] += 1
    for j in range(blinks):
        xdcp = defaultdict(int)
        for key in xd.keys():
            if key == 0:
                xdcp[1] += xd[key]
            elif len(str(key)) % 2 == 0:
                xdcp[int(str(key)[:len(str(key))//2])] += xd[key]
                xdcp[int(str(key)[len(str(key))//2:])] += xd[key]
            else:
                xdcp[2024 * key] += xd[key]
        xd = xdcp.copy()
    for val in xd.values():
        summed += val
    return summed
                
print("First: " + str(main("files/11", 25)))
print("Second: " + str(main("files/11", 75)))
