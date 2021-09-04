import collections

N = int(input())
S = [str(input()) for i in range(N)]

c = collections.Counter(S)
maxCount = c.most_common()[0][1]
ans = []
for e in c.most_common():
    if e[1] == maxCount:
        ans.append(e[0])
    else:
        break

for e in sorted(ans, reverse=False):
    print(e)


# SetS = set(S)
# CountS = []
# maxCount = 0
# for s in SetS:
#     cnt = S.count(s)
#     CountS.append([s, cnt])
#     maxCount = max(maxCount, cnt)

# # print(maxCount)
# # print(CountS)

# ansS = []
# for s in CountS:
#     if s[1] == maxCount:
#         ansS.append(s[0])
#     if s[1] < maxCount:
#         break

# # print(ansS)
# sortedansS = sorted(ansS, reverse=False)

# for s in sortedansS:
#     print(s)
