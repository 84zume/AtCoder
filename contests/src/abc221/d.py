import collections
N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]

t = collections.OrderedDict()

for e in AB:
    a = str(e[0])
    b = str(e[0]+e[1])

    if a not in t:
        t[a] = 1
    else:
        t[a] += 1

    if b not in t:
        t[b] = -1
    else:
        t[b] -= 1

# print(t)

t1 = collections.OrderedDict(
    sorted(t.items(), key=lambda x: x[0])
)
# print(t1)

# l = list(t1.items())
# imo =  [[0] * 2 for i in range(len(l))]
# for i in range(len(l)):
#     imo

imo = collections.OrderedDict()
pre_val = 0
for t_item in t1.items():
    # print(pre_val, t_item[1])
    imo[t_item[0]] = t_item[1] + pre_val
    pre_val = t_item[1] + pre_val

# print(imo)

ans = [0] * (N+1)

pre_key = 0
pre_val = 0
for imo_item in imo.items():
    key = int(imo_item[0])
    val = imo_item[1]
    ans[val] += (key - pre_key)
    pre_key = key

print(' '.join(map(str, ans[1:])))
