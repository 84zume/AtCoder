n, m = map(int, input().split())
k = [[int(j) for j in input().split()] for i in range(n)]

all = [0]*(m+1)

for a in k:
    for e in range(1, len(a)):
        all[a[e]] += 1
        # print(all)
print(all.count(n))
