N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]

result = [0] * N

for a in A:
    result[a-1] += 1

for r in result:
    r += (K - Q)
    if r <= 0:
        print('No')
    else:
        print('Yes')
