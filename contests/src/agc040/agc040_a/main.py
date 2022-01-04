#!/usr/bin/env python3
# from typing import *


# def solve(S: str) -> int:
def solve(S):
    a = [0]*(len(S)+1)

    for i in range(len(S)):
        if S[i] == '<':
            a[i+1] = max(a[i+1], a[i]+1)

    for i in reversed(range(len(S))):
        if S[i] == '>':
            a[i] = max(a[i], a[i+1]+1)

    return sum(a)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
