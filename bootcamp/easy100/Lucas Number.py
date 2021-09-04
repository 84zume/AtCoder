N = int(input())


# def Luca(n):
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         return Luca(n-1) + Luca(n-2)


L = [2, 1]

for i in range(2, N+1):
    L.append(L[i-2]+L[i-1])

print(L[N])
