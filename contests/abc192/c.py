N, K = map(int, input().split())


def g1(n):
    s = str(n)
    ss = sorted(s, reverse=True)
    # print(ss)
    return int(''.join(ss))


def g2(n):
    s = str(n)
    ss = sorted(s)
    # print(ss)
    return int(''.join(ss))


def f(n):
    return g1(n)-g2(n)


a = N
for i in range(K):
    a = f(a)
    # print(i+1, a)
print(a)
