#!/usr/bin/env python3
# from typing import *


# def solve(K: int) -> str:
def solve(K):
    bi = format(K, 'b')
    bi_str = str(bi)
    return bi_str.replace('1', '2')


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    K = int(input())
    a = solve(K)
    print(a)


if __name__ == '__main__':
    main()
