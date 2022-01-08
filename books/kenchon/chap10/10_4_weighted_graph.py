class Edge:
    def __init__(self, to, weight) -> None:
        self.to = to
        self.weight = weight

    def __str__(self):
        return str(self.to) + "(" + str(self.weight) + ")"

    def __repr__(self) -> str:
        return self.__str__()


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M - 1):
    a, b, w = input().split()
    edge = Edge(int(b), float(w))
    graph[int(a)].append(edge)

for i in range(N):
    print(i, "=", graph[i])
    # for g in graph[i]:
    #     print(g)

# 8 13
# 4 1 0.5
# 4 2 0.3
# 4 6 0.1
# 1 3 0.2
# 1 6 0.9
# 2 5 0.6
# 2 7 0.7
# 6 7 0.8
# 3 0 0.1
# 3 7 0.3
# 7 0 0.5
# 0 5 0.5
