N = int(input())
H = list(map(int, input().split()))

maxCnt = 0
n = 0
# while n < N:
#     cnt = 0
#     for s in range(n, N-1):
#         if H[s] >= H[s+1]:
#             cnt += 1
#         else:
#             n = s+1
#             break

#     # print('s:', s, 'cnt:', cnt)
#     print(n)
#     maxCnt = max(cnt, maxCnt)

i = 0
while i < N-1:
    cnt = 0
    s = i
    # print(s)
    # print('H[s]', H[s])
    # print('H[s+1]', H[s+1])
    while s < N-1 and H[s] >= H[s+1]:
        cnt += 1
        s += 1
        # print('while s: ', s)
    i = s+1
    maxCnt = max(maxCnt, cnt)


print(maxCnt)
