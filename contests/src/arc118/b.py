import numpy as np
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
np_sa = np.array(sa)
sumB2 = sum(tempB2)
if sumB2 != M:
    cnt = sumB2 - M
    while cnt > 0:
        i = np.argmin(np_sa)
        tempB2[i] -= 1
        np_sa[i] = 99999
        cnt -= 1
    while cnt < 0:
        i = np.argmax(np_sa)
        tempB2[i] += 1
        np_sa[i] = -99999
        cnt += 1
    ans = tempB2
else:
    ans = tempB2

print(' '.join(map(str, tempB2)))
