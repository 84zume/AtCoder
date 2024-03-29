#!/usr/bin/env python3
# from typing import *
import sys
sys.setrecursionlimit(100000)


def rec(A, T, K, task, sum, memo):

    if K[task-1] == 0:
        return 0

    if memo[task-1] != -1:
        return memo[task-1]

    tasks = A[task-1]
    for t in tasks:
        sum += T[t-1]
        rec(A, T, K, t, sum, memo)
    memo[t-1] = sum
    return sum

# def solve(n: int, a: List[int]) -> int:


def solve(N, T, K, A):
    memo = [-1]*N
    sum = T[N-1]
    sum = rec(A, T, K, N, sum, memo)
    return sum

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)


def main():
    # failed to analyze input format
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        temp = list(map(int, input().split()))
        T.append(temp[0])
        K.append(temp[1])
        A.append(temp[2:])
    a = solve(N, T, K, A)
    print(a)


if __name__ == '__main__':
    main()
