#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(n, m, a):
    x = a[0][0]
    youbi = x % 7
    if youbi == 0:
        youbi = 7

    for i in range(n):
        for j in range(m):
            if j+1 < m:
                if abs(a[i][j+1] - a[i][j]) != 1:
                    return 'No'
                if a[i][j+1] % 7 == 1 and a[i][j] % 7 == 0:
                    return 'No'
            if i+1 < n:
                if abs(a[i+1][j] - a[i][j]) != 7:
                    return 'No'
    return 'Yes'


def main():
    # failed to analyze input format
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = solve(n, m, a)
    print(ans)


if __name__ == '__main__':
    main()
