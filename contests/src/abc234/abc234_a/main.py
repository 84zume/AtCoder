#!/usr/bin/env python3
# from typing import *


def fx(x):
    return x**2 +2*x+3

# def solve(t: int) -> int:
def solve(t):
    return fx(fx(fx(t) + t) +fx(fx(t)))


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    t = int(input())
    a = solve(t)
    print(a)


if __name__ == '__main__':
    main()