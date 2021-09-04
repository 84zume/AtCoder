N = int(input())
W = [str(input()) for i in range(N)]

if len(set(W)) != N:
    print('No')
    exit(0)

start = W[0][-1]

for i in range(1, N):
    if W[i][0] != start:
        print('No')
        exit(0)
    start = W[i][-1]

print('Yes')
