N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

a1 = A[0][0] + sum(A[1][0:N])
an = sum(A[0][0:N]) + A[1][N-1]

maxAme = max(a1, an)

for i in range(1, N-1):
    ame = 0
    ame += sum(A[0][0:i+1])
    ame += sum(A[1][i:N])
    # print(ame)
    maxAme = max(maxAme, ame)

# print(a1)
# print(an)

print(maxAme)
