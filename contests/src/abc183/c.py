import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

l = []

for e in range(2, N+1):
    l.append(e)

cnt = 0

for v in itertools.permutations(l):
    v_list = list(v)
    v_list.append(1)
    v_list.insert(0, 1)
    # print(v_list)

    kyori = 0
    for i in range(len(v_list)-1):
        kyori += T[v_list[i]-1][v_list[i+1]-1]
    # print(kyori)
    if kyori == K:
        cnt += 1

print(cnt)
