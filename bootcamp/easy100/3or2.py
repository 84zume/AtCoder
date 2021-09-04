N = int(input())
a = list(map(int, input().split()))

ans = []

for e in a:
    cnt = 0
    while e % 2 == 0:
        e /= 2
        cnt += 1
    ans.append(cnt)
# print(ans)
# maxCnt = max(ans)
cnt = sum(ans)
# for e in ans:
#     cnt += (maxCnt - e)
print(cnt)
