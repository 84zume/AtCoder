N = int(input())
a = list(map(int, input().split()))


find = 1
for e in a:
    if e == find:
        find += 1
if find == 1:
    print(-1)
else:
    print(N-find+1)
