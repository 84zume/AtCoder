#!/usr/bin/env python3
# from typing import *

# def solve(N: int, W: int, A: List[int], B: List[int]) -> int:
def solve(N, W, A, B, AB):
    AB.sort(reverse=True)
    ans = 0
    index = 0
    while W > 0:
        a = AB[index][0]
        b = AB[index][1]
        if W >= b:
            ans += a*b
            W -= b
        else:
            ans += a*W
            W = 0
        index += 1
        if index >= N:
            break
    return ans


def main():
    N, W = map(int, input().split())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    AB = []
    for i in range(N):
        A[i], B[i] = map(int, input().split())
        AB.append([A[i], B[i]])
    a = solve(N, W, A, B, AB)
    print(a)


if __name__ == '__main__':
    main()
