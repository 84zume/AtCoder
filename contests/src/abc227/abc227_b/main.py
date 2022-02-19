#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: List[int]) -> int:
def solve(N, S):
    ans = []
    for a in range(1, 400):
        for b in range(1,400):
            ans.append(4*a*b+3*a+3*b)
    count = 0
    for s in S:
        if s in ans:
            count += 1
    return N-count

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
