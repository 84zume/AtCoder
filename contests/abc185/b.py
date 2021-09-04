n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]

nowtime = 0
maxn = n

for i in range(m):
    heru = a[i][0] - nowtime
    n = n - heru
#    print(i, 'Before', n)
    if n <= 0:
        print('No')
        exit(0)
    fueru = a[i][1] - a[i][0]
    n = n + fueru
    n = min(n, maxn)
#    print(i, 'After', n)
    nowtime = a[i][1]

heru = t - nowtime
n = n - heru
#print(i, 'Before', n)
if n <= 0:
    print('No')
    exit(0)
print('Yes')
