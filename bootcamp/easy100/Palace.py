N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

best = 10000000
mini = 0
for i in range(N):
    h = T - H[i]*0.006
    # print(h)
    sa = abs(A-h)
    if sa < best:
        best = sa
        mini = i+1
print(mini)
