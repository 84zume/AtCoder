#!/usr/bin/env python3
# from typing import *
import math

# def solve(X: int, Y: int) -> int:


def solve(X, Y):
    sa = Y-X
    if sa < 0:
        return 0
    else:
        ans = math.ceil(sa / 10)
        return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    X, Y = map(int, input().split())
    a = solve(X, Y)
    print(a)


if __name__ == '__main__':
    main()