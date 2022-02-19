#!/usr/bin/env python3
# from typing import *
import bisect
import copy


def solve(N, K, P):
    P4 = []

    for i in range(N):
        P4.append(sum(P[i]))

    sortedP4 = sorted(P4)

    result = []
    for p in P4:
        # temp_p = copy.copy(sortedP4)
        # temp_p.remove(p)
        temp_p = sortedP4
        rank = N - bisect.bisect(temp_p, p + 300)
        if rank+1 <= K:
            result.append('Yes')
        else:
            result.append('No')

    return result


def main():
    # failed to analyze input format
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        t1, t2, t3 = map(int, input().split())
        P.append([t1, t2, t3])

    ans = solve(N, K, P)

    for a in ans:
        print(a)  # TODO: edit here


if __name__ == '__main__':
    main()
