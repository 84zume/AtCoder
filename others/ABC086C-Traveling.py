import copy


def get_next_block(now):
    next = []
    # x+1
    next.append((now[0]+1, now[1]))

    # x-1
    if(now[0] != 0):
        next.append((now[0]-1, now[1]))

    # y+1
    next.append((now[0], now[1]+1))

    # y-1
    if(now[1] != 0):
        next.append((now[0], now[1]-1))

    return next


n = int(input())
p = [[int(j) for j in input().split()] for i in range(n)]

search = [(0, 0)]
cnt = 0
find = True

while True:
    tmp_search = copy.copy(search)
    search.clear()

    if p[0][0] == cnt:
        if (p[0][1], p[0][2]) in tmp_search:
            find = True
            tmp_search.clear()
            tmp_search = [(p[0][1], p[0][2])]
            p.pop(0)
        else:
            find = False
            break

    if(len(p) == 0):
        break

    cnt += 1

    for e in tmp_search:
        next = get_next_block(e)
        search.extend(next)
        search = list(set(search))

if(find):
    print('Yes')
else:
    print('No')
