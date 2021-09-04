import math
N = int(input())

maxn = int(math.floor(N**0.5))

# cnt = 0
ok = []

for i in range(2, maxn+1):
    j = 2
    while i**j <= N:
        # print(i**j)
        # cnt += 1
        ok.append(i**j)
        j += 1

print(N-len(set(ok)))
