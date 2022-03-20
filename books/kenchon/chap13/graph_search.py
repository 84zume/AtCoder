from collections import deque


def search(g, top):
    N = len(g)

    seen = [False] * N
    todo = deque()

    seen[top] = True
    todo.append(top)

    while len(todo) != 0:
        v = todo.popleft()

        for x in g[v]:
            if seen[x]:
                continue
            seen[x] = True
            todo.append(x)


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(M - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
    search(graph, graph[0])

"""
8 13
4 1
4 2
4 6
1 3
1 6
2 5
2 7
6 7
3 0
3 7
7 0
0 5
"""
