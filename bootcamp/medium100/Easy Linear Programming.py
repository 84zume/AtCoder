a, b, c, k = map(int, input().split())

count = 0
sumval = 0
while k > 0:
    if k >= a:
        sumval += k
        k -= a
        a = 0
    elif a > 0:
        sumval += 1
        k -= 1
        a -= 1
    elif k >= b:
        k -= b
        b = 0
    elif b > 0:
        k -= 1
        b -= 1
    elif k >= c:
        sumval -= k
        k -= c
        c = 0
    elif c > 0:
        sumval -= 1
        k -= 1
        c -= 1
    else:
        break
    print(a, b, c, k)
print(sumval)
