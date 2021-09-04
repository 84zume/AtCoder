N = int(input())
# K = [list(map(int, input().split())) for i in range(N)]

K = []
for i in range(N):
    t = list(map(int, input().split()))
    if t[0] == 1:
        K.append([t[1], t[2]])
    elif t[0] == 2:
        K.append([t[1], t[2]-0.1])
    elif t[0] == 3:
        K.append([t[1]+0.1, t[2]])
    elif t[0] == 4:
        K.append([t[1]+0.1, t[2]-0.1])


def common_kukan(k1, k2):
    if (k1[1] >= k2[0] and k1[0] < k2[1]) or (k1[0] <= k2[1] and k2[0] < k1[1]):
        return True
    else:
        return False


cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if common_kukan(K[i], K[j]):
            # print(K[i], K[j], 'OK')
            cnt += 1
        # else:
        #     print(K[i], K[j], 'NG')

print(cnt)
