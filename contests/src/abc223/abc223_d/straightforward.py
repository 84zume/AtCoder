#!/usr/bin/env python3
# from typing import *
import numpy as np
import pandas as pd

# def solve(N: int, M: int, A: List[int], B: List[int]) -> Any:


def solve(N, M, A, B):

    AB = []
    for i in range(M):
        AB.append(list(A[i]) + list(B[i]))
    print(AB)

    # A_t = (np.array(A).T).tolist()
    # B_t = (np.array(B).T).tolist()
    # print(A_t)
    # ans = ''

    # a = sorted(list(set(A_t)))
    # print(a)
    # ans += " ".join(map(str, a))

    # b = sorted(list(set(B_t)))
    # ans += " ".join(map(str, b))

    AB_t = (np.array(AB).T).tolist()

    ans = ''
    print(AB_t)
    for e in AB_t:
        print(e)
        ans += " ".join(sorted(list(set(e))))

    print(ans)

    return ans

    # max_len_A = len(max(A))
    # idx = 0
    # for a in A:
    #     a[idx]

    # u = set(A+B)
    # for e in itertools.permutations(u, len(u)):
    #     # print("星", "".join(map(str, e)))
    #     check = True
    #     for i in range(M):
    #         if e.index(A[i]) > e.index(B[i]):
    #             check = False
    #             # break
    #     if check == True:
    #         return " ".join(map(str, e))
    # return -1

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)


def main():
    N, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(str, input().split())
    ans = solve(N, M, A, B)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()
