#!/usr/bin/env python3
# from typing import *


# def solve(Q: int, t: List[int], x: List[int]) -> Tuple[int, int]:
def solve(Q, t, x, h):
    A = [-1] * (2**20+1)
    result = []
    for i in range(Q):
        if t[i] == 1:
            index = x[i]
            while A[index] != -1:
                index += 1
            A[index] = h[i]
        else:
            index = x[i]
            result.append(A[index])

    return result


def main():
    Q = int(input())
    t = [None for _ in range(Q)]
    x = [None for _ in range(Q)]
    h = [None for _ in range(Q)]
    for i in range(Q):
        p1, p2 = map(int, input().split())
        t[i] = p1
        x[i] = p2 % 2**20
        h[i] = p2
    ans = solve(Q, t, x, h)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
