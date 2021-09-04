n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(n):
    l.append([i+1, a[i]])

sl = sorted(l, key=lambda x: x[1])
sl0 = [r[0] for r in sl]
print(' '.join([str(_) for _ in sl0]))
