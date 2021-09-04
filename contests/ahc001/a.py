def findy(y, l):
    for e in l:
        if e[1] == y:
            return e
    return False


n = int(input())
xyr = [list(map(int, input().split())) for i in range(n)]

ans = []

for e in xyr:
    a = e[0]
    b = e[1]
    c = e[0]+1
    d = e[1]+1
    ans.append([a, b, c, d])

# print('---')
# for e in ans:
#     print(e[0], e[1], e[2], e[3])
# print('---')

ans2 = []

for e in ans:
    # y座標
    x1 = e[0]
    y1 = e[1]
    x2 = 10000
    y2 = e[3]
    ans = sorted(ans, key=lambda x: x[0], reverse=True)
    for a in ans:
        # print('★', a[0], a[1])
        # X軸プラス方向に伸ばせるだけ伸ばすパターン
        # 接した and 自分より大きい and 自分以外
        if (a[1] == y1) and (x1 < a[0]) and not(a[0] == x1 and a[1] == y1):
            x2 = a[0]
    ans2.append([e[0], e[1], x2, e[3]])

# print('---')
# for e in ans2:
#     print(e[0], e[1], e[2], e[3])
# print('---')

ans3 = []

for e in ans2:
    # y座標
    x1 = 0
    y1 = e[1]
    x2 = e[2]
    y2 = e[3]
    ans2 = sorted(ans2, key=lambda x: x[0], reverse=False)
    for a in ans2:
        # X軸マイナス方向に伸ばせるだけ伸ばすパターン
        # 接した and 自分より小さい and 自分以外
        if (a[1] == y1) and (a[2] <= e[0]) and not(a[0] == e[0] and a[1] == y1):
            x1 = a[2]
    ans3.append([x1, e[1], e[2], e[3]])

# for e in ans3:
#     print(e[0], e[1], e[2], e[3])

ans4 = []

# 上のパターン
for e in ans3:
    # y座標
    x1 = e[0]
    y1 = e[1]
    x2 = e[2]
    y2 = e[3]
    ans3 = sorted(ans3, key=lambda x: x[1], reverse=True)
    for a in ans3:
        # Y軸プラス方向に伸ばせるだけ伸ばすパターン
        # 自分以外
        if (e[1] < a[1]):
            y2 = a[1]
    ans4.append([x1, y1, x2, y2])

# for e in ans4:
#     print(e[0], e[1], e[2], e[3])

ans5 = sorted(ans4, key=lambda x: x[1], reverse=False)
m = ans5[0]

print(m[0], 0, m[2], m[3])

for i in range(1, len(ans5)):
    print(ans5[i][0], ans5[i][1], ans5[i][2], ans5[i][3])
