#!/usr/bin/env python3
# from typing import *

MOD = 1000000007


# def solve(N: int, A: int, B: int, S: List[int]) -> int:
def solve(N, A, B, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, A, B = map(int, input().split())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = int(input())
    a = solve(N, A, B, S)
    print(a)


if __name__ == '__main__':
    main()
