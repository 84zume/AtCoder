N = int(input())
A = list(map(int, input().split()))
index_half = int(len(A)/2)

A1 = A[0:index_half]
A2 = A[index_half:]

# print('A1:', A1)
# print('A2:', A2)

maxA1 = max(A1)
maxA2 = max(A2)
ans = 0
if maxA1 >= maxA2:
    ans = maxA2
else:
    ans = maxA1
# print('ans=', ans)
ans_index = A.index(ans)
print(ans_index+1)
