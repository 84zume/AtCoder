N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AllMons = sum(A)

for i in reversed(range(1, N+1)):
    sa1 = 0
    sa2 = 0
    if A[i] >= B[i-1]:
        sa1 = B[i-1]

        A[i] -= sa1
        B[i-1] -= sa1

    else:
        sa1 = A[i]

        A[i] -= sa1
        B[i-1] -= sa1

        if A[i-1] >= B[i-1]:
            sa2 = B[i-1]

            A[i-1] -= sa2
            B[i-1] -= sa2

        else:
            sa2 = A[i-1]
            A[i-1] -= sa2
            B[i-1] -= sa2
# print(A)
# print(B)
print(AllMons - sum(A))
