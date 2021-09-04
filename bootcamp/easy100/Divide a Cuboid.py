import math


def cube(A, B, C):
    return A * B * C


A, B, C = map(int, input().split())

if A >= B and A >= C:
    print(cube(math.ceil(A/2), B, C) - cube(math.floor(A/2), B, C))

elif B >= A and B >= C:
    print(cube(math.ceil(B/2), A, C) - cube(math.floor(B/2), A, C))

elif C >= A and C >= B:
    print(cube(math.ceil(C/2), A, B) - cube(math.floor(C/2), A, B))
