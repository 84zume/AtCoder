import itertools

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for i in range(K)]

max_cnt = 0

for ds in itertools.product(*CD):
    ball = set(ds)
    cnt = 0
    for d in AB:
        if d[0] in ball and d[1] in ball:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)

# temp_ball = [0]*N
# for b in CD:
#     if temp_ball.count(b[0]) == 0:
#         temp_ball.append(b[0])
#     else:
#         temp_ball.append(b[1])
# ball = sorted(set(temp_ball))
# # print('ball:', ball)


# cnt = 0
# for d in AB:
#     if ball.count(d[0]) > 0 and ball.count(d[1]) > 0:
#         cnt += 1

# print(cnt)
