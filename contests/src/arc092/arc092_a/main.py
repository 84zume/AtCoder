#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
def solve(N, red, blue):
    # red.sort()
    blue.sort()
    used = [0]*N

    # 青を基準に探索
    for i in range(N):
        maxy = -1
        maxid = -1
        for j in range(N):
            if used[j] == 1:
                continue
            if red[j][0] > blue[i][0]:
                continue
            if red[j][1] > blue[i][1]:
                continue

            if red[j][1] > maxy:
                maxy = red[j][1]
                maxid = j
        if maxid == -1:
            continue
        used[maxid] = 1
    return sum(used)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    red = []
    blue = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        red.append(tuple(temp))

    for _ in range(N):
        temp = list(map(int, input().split()))
        blue.append(tuple(temp))

    a1 = solve(N, red, blue)
    print(a1)


if __name__ == '__main__':
    main()
