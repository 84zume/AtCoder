def search(head_node, now_node, route, result):
    if [head_node, now_node] in result:
        return
    else:
        result.append([head_node, now_node])

    next_route = list(filter(lambda x: x[0] == now_node, route))
    if len(next_route) == 0:
        return

    for r in next_route:
        search(head_node, r[1], route, result)


N, M = map(int, input().split())
R = [list(map(int, input().split())) for i in range(M)]

result = []
for i in range(1, N+1):
    search(i, i, R, result)

print(len(result))
