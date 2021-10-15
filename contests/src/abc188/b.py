import numpy as np

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if np.dot(A, B) == 0:
    print('Yes')
else:
    print('No')
