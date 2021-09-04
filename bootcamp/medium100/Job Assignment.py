N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

minA_index = A.index(min(A))
minB_index = B.index(min(B))


if minA_index == minB_index:
    pa = min(A)+min(B)
else:
    pb = max(min(A), min(B))
