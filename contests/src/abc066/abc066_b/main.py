#!/usr/bin/env python3
# from typing import *

def solve(S):
    S = S[:-1]
    l = len(S)
    while l > 0:
        if l % 2 == 0:
            if S[0:int(l/2)-1] == S[int(l/2):l-1]:
                return l
        l -= 1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)


def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()