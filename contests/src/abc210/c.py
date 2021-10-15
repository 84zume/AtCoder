N, K = map(int, input().split())
c = list(map(int, input().split()))

lenc = len(set(c))

max_size = 0

mydict = {}


for i in range(K):
    if c[i] in mydict:
        mydict[c[i]] += 1
    else:
        mydict[c[i]] = 1


max_size = len(mydict)

for i in range(K, N):
    # print(c[i], mydict)
    if c[i] in mydict:
        mydict[c[i]] += 1
    else:
        mydict[c[i]] = 1

    mydict[c[i-K]] -= 1

    if mydict[c[i-K]] == 0:
        del(mydict[c[i-K]])

    max_size = max(max_size, len(mydict))

print(max_size)
