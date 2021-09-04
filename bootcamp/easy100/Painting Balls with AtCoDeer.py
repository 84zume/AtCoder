N, K = map(int, input().split())

p = K
for i in range(N-1):
    p *= (K-1)
print(p)
