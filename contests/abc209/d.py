import queue


def BFS(townmap, N, start, end):
    q = queue.Queue()
    q.put(start)
    step = 0
    visited = [0]*(N+1)
    while(not q.empty()):
        v = q.get()
        step += 1
        print('Visit', v)

        if visited[v] == 1:
            print('Skip')
            continue

        visited[v] = 1
        if v == end:
            print(step)
            return step

        for i in range(N+1):
            if townmap[v][i] == 1:
                print('候補', i)
                q.put(i)
                step -= 1


N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N-1)]
CD = [list(map(int, input().split())) for i in range(Q)]

townmap = [[0] * (N+1) for i in range(N+1)]
for ab in AB:
    townmap[ab[0]][ab[1]] = 1
    townmap[ab[1]][ab[0]] = 1

for t in townmap:
    print(t)

BFS(townmap, N, 7, 8)

# for cd in CD:
#     kyori = BFS(townmap, N, cd[0], cd[1])
#     if kyori % 2 == 0:
#         print('Town')
#     else:
#         print('Road')
