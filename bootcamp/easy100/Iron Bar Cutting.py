N = int(input())
L = list(map(int, input().split()))

mean = sum(L) / 2
cnt = 0
for i, j in enumerate(L):
    cnt += j
    # カウンタが中央値を超えた時
    if cnt >= mean:
        # カウンタと中央値の差
        # 一つ前のindexのカウンタ(+jで再現)と中央値の差
        # 上記のうち小さい方に2を掛ける
        res = int(min(cnt - mean, mean - cnt + j) * 2)
        break
print(res)
