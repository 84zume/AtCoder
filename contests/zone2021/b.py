N, D, H = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

min_k = 1000
min_index = 0
for i in range(len(X)):
    k = (X[i][1]-H) / (X[i][0]-D)
    if min_k > k:
        min_k = k
        min_index = i

b = max(H-min_k*D, 0)

print(b)
