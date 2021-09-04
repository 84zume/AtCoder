import collections

N = int(input())
s = [str(input()) for i in range(N)]
M = int(input())
t = [str(input()) for i in range(M)]

cs = collections.Counter(s)
ct = collections.Counter(t)

ans = []

for e in cs.items():
    # print(e[0], e[1], ct[e[0]])
    if ct[e[0]] > 0:
        ans.append([e[0], e[1] - ct[e[0]]])
    else:
        ans.append([e[0], e[1]])

result = max(ans, key=(lambda x: x[1]))[1]

if result >= 0:
    print(result)
else:
    print(0)
