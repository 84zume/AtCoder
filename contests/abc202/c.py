import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = 0
# for i in range(N):
#     for j in range(N):
#         if A[i] == B[C[j]-1]:
#             cnt += 1
# print(cnt)


B1 = []
for i in range(N):
    B1.append(B[C[i]-1])
# print('B1', B1)
# cnt = 0
# for a in A:
#     cnt += B1.count(a)
# print(cnt)

collection_A = collections.Counter(A)
collection_B1 = collections.Counter(B1)

cnt = 0
for k in collection_A.keys():
    cnt += collection_A[k] * collection_B1[k]
print(cnt)
