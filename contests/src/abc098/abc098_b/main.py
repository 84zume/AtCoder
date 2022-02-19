#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: str) -> int:
def solve(N, S):
    i = 1
    count = 0
    while i < N:
        X = set(S[:i])
        Y = set(S[i:])
        Z = X & Y
        count = max(count, len(list(Z)))
        i += 1
    return count


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == "__main__":
    main()
