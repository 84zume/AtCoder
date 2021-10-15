K, N, M = map(int, input().split())
A = list(map(int, input().split()))

wariai = M/N
tempB2 = []
sa = []
for i in range(K):
    tempB2.append(round(A[i]*wariai))
    if A[i]*wariai < round(A[i]*wariai):
        sa.append(-abs(round(A[i]*wariai)/M-A[i]/N))
    else:
        sa.append(abs(round(A[i]*wariai)/M-A[i]/N))

# for i in range(K):
#     print(tempB1[i], tempB2[i], sa[i])
# print(max(sa))

if sum(tempB2) != M:
    cnt = sum(tempB2) - M
    while cnt > 0:
        i = sa.index(min(sa))
        tempB2[i] -= 1
        sa[i] = 0
        cnt -= 1
    while cnt < 0:
        i = sa.index(max(sa))
        tempB2[i] += 1
        sa[i] = 0
        cnt += 1
    ans = tempB2
else:
    ans = tempB2

print(' '.join(map(str, tempB2)))
# print(sum(tempB2))

# sa2 = []
# for i in range(K):
#     print(abs(ans[i]/M-A[i]/N))
#     sa2.append(abs(ans[i]/M-A[i]/N))

# print(max(sa2))
