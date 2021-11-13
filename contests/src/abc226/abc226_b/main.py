#!/usr/bin/env python3
# from typing import *


# def solve(a: int, b: List[int], c: List[List[int]]) -> int:
def solve(N, L, a):
    ans = [0] * N
    set_a = list(map(list, set(map(tuple, a))))
    return len(set_a)

    # print(len(set_a)
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if ans[j] == 1:
    #             continue
    #         if L[i] != L[j]:
    #             continue
    #         if a[i] == a[j]:
    #             ans[j] = 1
    # return ans.count(0)


def main():
    N = int(input())
    L = []
    a = []
    for i in range(N):
        temp = list(map(int, input().split()))
        L.append(temp[0])
        a.append(temp[1:])

    a1 = solve(N, L, a)
    print(a1)


if __name__ == '__main__':
    main()
