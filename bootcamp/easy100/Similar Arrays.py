import itertools

N = int(input())
A = list(map(int, input().split()))

l = [-1, 0, 1]
# c = itertools.combinations_with_replacement(l, N)
c = itertools.product(l, repeat=N)
# for v in c:
#     print(v)

count = 0
for v in c:
    seki = 1
    for i in range(N):
        seki *= (A[i] + v[i])
    # print(seki)
    if seki % 2 == 0:
        count += 1
print(count)
