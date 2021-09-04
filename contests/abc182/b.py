n = int(input())
a = list(map(int, input().split()))

gcd = {}
for i in range(2, max(a)+1):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    gcd[i] = cnt
    #gcd.append((i, cnt))
   # print(i)

print(max(gcd, key=(lambda x: gcd[x])))
