import itertools

N = list(input())

P = itertools.permutations(N)

maxval = 0

for p in P:
    # print('★', p)
    for i in range(1, len(p)):
        a = int("".join(p[:i]))
        b = int("".join(p[i:]))
        # print(a, b)
        maxval = max(maxval, a*b)
print(maxval)
