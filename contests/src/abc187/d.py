import numpy as np
N = int(input())

A = []

aoki = 0
for i in range(N):
    a, b = map(int, input().split())
    aoki += a
    A.append([a, b, a+b])

# A_sorted2 = sorted(A, key=lambda x: (x[0]), reverse=True)
A_sorted2 = sorted(A, key=lambda x: (x[2], x[1]), reverse=True)
# print(A_sorted2)

takahashi = 0
for i in range(len(A_sorted2)):
    takahashi += A_sorted2[i][2]
    aoki -= A_sorted2[i][0]
    # print(takahashi, aoki)
    if(takahashi > aoki):
        print(i+1)
        exit(0)
