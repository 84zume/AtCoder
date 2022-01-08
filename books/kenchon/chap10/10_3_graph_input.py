N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(N):
    print(i, "=", graph[i])

# 8 13
# 4 1
# 4 2
# 4 6
# 1 3
# 1 6
# 2 5
# 2 7
# 6 7
# 3 0
# 3 7
# 7 0
# 0 5
