N = int(input())
A = list(map(int, input().split()))
A1 = sorted(A)
for i in range(N):
    if A1[i] != i+1:
        print('No')
        exit(0)
print('Yes')
