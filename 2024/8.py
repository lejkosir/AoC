def remake(filename):
    ant_dict = {}
    with open(filename) as file:
        for y, line in enumerate(file):
            for x, ch in enumerate(line[:-1]):
                if ch != ".":
                    if ch in ant_dict:
                        ant_dict[ch].append((y, x))
                    else:
                        ant_dict[ch] = [(y, x)]

        return ant_dict, y, x

def first(filename):
    antinodes= set()
    ant_dict, y_lim, x_lim  = remake(filename)
    print(ant_dict)
    for key, value in ant_dict.items():
        for antenna in value:
            for comparison in value:
                if antenna != comparison:
                    dist = (antenna[0] - comparison[0], antenna[1] - comparison[1])
                    antinode = (antenna[0] + dist[0], antenna[1] + dist[1])
                    if y_lim >= antinode[0] >= 0 and x_lim >= antinode[1] >= 0:
                        antinodes.add(antinode)
    print(len(antinodes))

# first z dodanim while loopom
def second(filename):
    antinodes = set()
    ant_dict, y_lim, x_lim = remake(filename)
    print(ant_dict)
    for key, value in ant_dict.items():
        for antenna in value:
            for comparison in value:
                if antenna != comparison:
                    antinode = antenna
                    antinodes.add(antinode)
                    while y_lim >= antinode[0] >= 0 and x_lim >= antinode[1] >= 0:
                        dist = (antenna[0] - comparison[0], antenna[1] - comparison[1])
                        antinode = (antinode[0] + dist[0], antinode[1] + dist[1])
                        if y_lim >= antinode[0] >= 0 and x_lim >= antinode[1] >= 0:
                            antinodes.add(antinode)
    print(len(antinodes))
first("files/8")
second("files/8")