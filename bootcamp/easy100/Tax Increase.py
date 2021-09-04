import math

A, B = map(int, input().split())

for i in range(1, 1009):
    tax8 = math.floor(i * 0.08)
    tax10 = math.floor(i * 0.10)

    if tax8 == A and tax10 == B:
        print(i)
        exit(0)
print(-1)

# # NA = math.floor(A / 0.08)
# # NB = math.floor(B / 0.10)

# NA = A/0.08
# NB = B/0.10

# # A1 = NA * 1.08
# # B1 = NB * 1.10

# print(NA, NB)

# if NA == NB:
#     print(NA)
# else:
#     print(-1)
