n, y = map(int, input().split())

sum = 0
val = n
notfound = True
for e1 in reversed(range(val+1)):
    a = e1
    b = val - e1
    for e2 in reversed(range(b + 1)):
        c = e2
        d = b - e2
        sum = 10000 * a + 5000 * c + 1000 * d
        if sum == y:
            print(a, c, d)
            notfound = False
            break
    else:
        continue
    break

if notfound:
    print(-1, -1, -1)
