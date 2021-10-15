N = int(input())
A = [int(i) for i in input().split()]

max_sum = 0

for i in range(N):
    tate = A[i]
    R = 0
    L = 0
    for R in range(i, N):
        if A[R] < tate:
            R = R-1
            break
    for L in reversed(range(i+1)):
        if A[L] < tate:
            L = L+1
            break
    rect = (R-L+1)*tate
    # print('i:', i, ' L:', L, 'R: ', R, ' A[i](x):', A[i], ' rect:', rect)
    max_sum = max(max_sum, rect)

print(max_sum)
