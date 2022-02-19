#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int) -> str:
def solve(A, B):
    a = str(A)
    b = str(B)
    # minlen = min(len(a), len(a))
    maxlen = max(len(a), len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    # print(a)
    # print(b)
    ans = False
    for i in reversed(range(maxlen)):
        c = int(a[i]) + int(b[i])
        # print(a[i], b[i], c)
        if c >= 10:
            ans = True

    if ans == False:
        return 'Easy'
    else:
        return 'Hard'

    # maxlen = max(len(str(A)), len(str(B)))
    # anslen = len(str(A+B))
    # if maxlen == anslen:
    #     return 'Easy'
    # else:
    #     return 'Hard'


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
