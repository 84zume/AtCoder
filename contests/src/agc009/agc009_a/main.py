#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: List[int], B: List[int]) -> int:
def solve(N, A, B):
    count = 0
    for i in range(N-1, -1, -1):
        A[i] += count
        amari = A[i] % B[i]
        d = 0
        if amari != 0:
            d = B[i] - amari
        count += d
    return count


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    a = solve(N, A, B)
    print(a)


if __name__ == '__main__':
    main()