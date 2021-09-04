N = int(input())
P = list(map(int, input().split()))

count = 0
m = 200000

for i in range(N):
    m = min(P[i], m)
    if P[i] <= m:
        count += 1
    # flag = True
    # if P[i] <= min(P[:i]):
    #     # print('#', i)
    #     count += 1
print(count)
