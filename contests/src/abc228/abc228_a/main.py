#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(S: int, T: int, X: int) -> str:
def solve(S, T, X):
    if S <= X and X < T:
        return YES

    if S > T:
        if S <= X and X <= 23:
            return YES
        if X < T:
            return YES
    return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S, T, X = map(int, input().split())
    a = solve(S, T, X)
    print(a)


if __name__ == '__main__':
    main()
