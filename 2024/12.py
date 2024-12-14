from collections import defaultdict

def remake(filename):
    with open(filename) as file:
        l = []
        for line in file:
            l.append(line[:-1])
    return l


# prvo preisce vse in v field_dict zapise razlicne njive (dfsearch)
# potem za vsako njivo poisce vse kote (corner_search)
def first(filename):
    l = remake(filename)
    summed1 = 0
    summed2 = 0
    visited = set()
    field_dict = defaultdict(list)
    field_count = defaultdict(int)
    fence_len = defaultdict(int)
    fence_len2 = defaultdict(int)
    for y, line in enumerate(l):
        for x, ch in enumerate(line):
            if (y, x) not in visited:
                field_count[ch] += 1
                dfsearch((y,x), l, visited, field_dict, field_count, fence_len, fence_len2)

    for key, value in field_dict.items():
        for coord in value:
            corner_search(coord, l, fence_len2, key)

    for key, value in field_dict.items():
        print(key, value, fence_len[key], fence_len2[key])
        summed1 += len(value) * fence_len[key]
        summed2 += len(value) * fence_len2[key]
    print(summed1, summed2)



# za dfsearch    ^       <        v        >
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# za corner_search       ^       <         v       >       <^        <v       v>      ^>
directions_corners = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]

# DFS
def dfsearch(coords, l, visited, field_dict, field_count, fence_len, fence_len2):
    if coords in visited:
        return
    #    ^   <  v  >
    xd = [1, 1, 1, 1]
    visited.add(coords)
    y, x = coords
    ch = l[y][x]
    for i, (dy, dx) in enumerate(directions):
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0:
            fence_len[ch + str(field_count[ch])] += 1
            xd[i] = 0
        else:
            try:
                if l[ny][nx] == ch:
                    dfsearch((ny, nx), l, visited, field_dict, field_count, fence_len, fence_len2)
                else:
                    xd[i] = 0
                    fence_len[ch + str(field_count[ch])] += 1
            except IndexError:
                xd[i] = 0
                fence_len[ch + str(field_count[ch])] += 1
                continue
    field_dict[ch+str(field_count[ch])].append((y,x))



def corner_search(coords, l, fence_len2, key):
    #    ^   <  v  > <^ <v  v> ^>
    xd = [1, 1, 1, 1, 1, 1, 1, 1]
    y, x = coords
    ch = l[y][x]

    for i, (dy, dx) in enumerate(directions_corners):
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0:
            xd[i] = 0
        else:
            try:
                if l[ny][nx] != ch:
                    xd[i] = 0
            except:
                xd[i] = 0

    if sum(xd[:4]) == 1:
        fence_len2[key] += 2
# zelo lepo
    else:
        for i, xa in enumerate(xd[4:]):
            if i == 0 and xa == 0:
                if (xd[0] == 1 and xd[1] == 1) or (xd[0] == 0 and xd[1] == 0):
                    fence_len2[key] += 1
            elif i == 0 and xa:
                if xd[0] == 0 and xd[1] == 0:
                    fence_len2[key] += 1
            if i == 1 and xa == 0:
                if (xd[1] == 1 and xd[2] == 1) or (xd[1] == 0 and xd[2] == 0):
                    fence_len2[key] += 1
            elif i == 1 and xa:
                if xd[1] == 0 and xd[2] == 0:
                    fence_len2[key] += 1
            if i == 2 and xa == 0:
                if (xd[2] == 1 and xd[3] == 1) or (xd[2] == 0 and xd[3] == 0):
                    fence_len2[key] += 1
            elif i == 2 and xa:
                if xd[2] == 0 and xd[3] == 0:
                    fence_len2[key] += 1
            if i == 3 and xa == 0:
                if (xd[0] == 1 and xd[3] == 1) or (xd[0] == 0 and xd[3] == 0):
                    fence_len2[key] += 1
            elif i == 3 and xa:
                if xd[0] == 0 and xd[3] == 0:
                    fence_len2[key] += 1


first("files/12")