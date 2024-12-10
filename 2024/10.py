def remake(filename):
    with open(filename) as file:
        map_dict = {}
        map_list = []
        for y, line in enumerate(file):
            map_list.append(line[:-1])
            for x, ch in enumerate(line[:-1]):
                if ch in map_dict:
                    map_dict[ch].append((y, x))
                else:
                    map_dict[ch] = [(y, x)]
    return map_dict, map_list

def main(filename):
    map_dict, map_list = remake(filename)
    summed = 0
    summed_paths = 0
    for coords in map_dict["0"]:
        counter = 0
        nines = set()
        summed_paths += rec(counter, map_list, coords, nines)
        summed += len(nines)
    print("First: " + str(summed))
    print("Second: " + str(summed_paths))


def rec(counter, map_list, coords, nines):
    counter += 1
    near = []
    try:
        if map_list[coords[0]][coords[1]+1] == str(counter) and coords[0] >= 0 and coords[1] +1 >= 0:
            near.append((coords[0], coords[1]+1))
    except:
        pass
    try:
        if map_list[coords[0]+1][coords[1]] == str(counter) and coords[0]+1 >= 0 and coords[1] >= 0:
            near.append((coords[0]+1, coords[1]))
    except:
        pass
    try:
        if map_list[coords[0]][coords[1]-1] == str(counter) and coords[0] >= 0 and coords[1] - 1 >= 0:
            near.append((coords[0], coords[1]-1))
    except:
        pass
    try:
        if map_list[coords[0]-1][coords[1]] == str(counter) and coords[0] - 1 >= 0 and coords[1] >= 0:
            near.append((coords[0]-1, coords[1]))
    except:
        pass
    if counter == 9:
        for x in near:
            nines.add(x)
    if counter == 10:
        return 1
    else:
        path_counter = 0
        for coord in near:
            path_counter += rec(counter, map_list, coord, nines)
        return path_counter

main("files/10")