#!/usr/bin/env python3
# from typing import *
import itertools

YES = 'Yes'
NO = 'No'


# def solve(N: str, M: str, A: List[str], B: List[str], C: List[str], D: List[str]) -> str:
def solve(N, M, A, B, C, D):
    base_p = []
    for i in range(N):
        base_p.append(i+1)

    all_p = itertools.permutations(base_p, N)

    for p in all_p:

        X = []
        Y = []
        for i in range(M):
            if p[C[i]-1] > p[D[i]-1]:
                Y.append([p[D[i]-1], p[C[i]-1]])
            else:
                Y.append([p[C[i]-1], p[D[i]-1]])
            X.append([A[i], B[i]])

        X.sort()
        Y.sort()
        check = True
        for i in range(M):
            if X[i][0] != Y[i][0] or X[i][1] != Y[i][1]:
                check = False
        if check:
            return YES
    return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    C = [None for _ in range(M)]
    D = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    a = solve(N, M, A, B, C, D)
    print(a)


if __name__ == '__main__':
    main()
