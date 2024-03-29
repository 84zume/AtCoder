#!/usr/bin/env python3
# from typing import *


# def solve(X: int) -> int:
def solve(X):
    # 2桁は等差数
    if X < 100:
        return X

    # 全て同じ桁ならば等差数
    if len(set(list(str(X)))) == 1:
        return X

    if X > 9876543210:
        lenX = len(str(X))
        return "".join(["1"] * (lenX + 1))


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    X = int(input())
    a = solve(X)
    print(a)


if __name__ == "__main__":
    main()
