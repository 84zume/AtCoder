import sys

sys.setrecursionlimit(10000)


def memoize(f):
    memo = {}

    def function(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]

    return function


@memoize
def Ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ack(m - 1, 1)
    return Ack(m - 1, Ack(m, n - 1))


def Ack2(m, n):
    stack = []
    stack.append(m)
    while stack:
        m = stack.pop()
        if m == 0 or n == 0:
            n += m + 1
        else:
            stack.append(m - 1)
            stack.append(m + 1)
            n -= 1
    return n


def main():
    # M = 5
    # N = 5
    # memo = [[-1] * 100 for i in range(100)]

    # for i in range(M):
    #     for j in range(N):
    #         print(i, j, Ack(i, j, memo))
    # print(Ack(3, 4, memo))
    # print(Ack2(4, 1))
    M, N = map(int, input().split())
    print(Ack(M, N))


if __name__ == "__main__":
    main()
