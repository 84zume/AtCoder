#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(n: int) -> str:
def solve(n):
    if 2**n > n**2:
        return YES
    else:
        return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    a = solve(n)
    print(a)


if __name__ == '__main__':
    main()