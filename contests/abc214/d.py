N = int(input())
W = []
for n in range(N-1):
    u, v, w = map(int, input().split())
    W.append(w)

W = sorted(W)

result = 0
for i in range(N-1):
    result += (W[i]*(i+1))
    print('XX', W[i], (i+1))

print(result)
