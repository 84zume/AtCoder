import math
X = int(input())

if X == 1 or X == 2 or X == 3:
    print(1)
    exit(0)

# sosuu = [2]
# A = X
# for L in range(3, A, 2):  # 2 以外の素数は奇数なので
#     if all(L % L2 != 0 for L2 in sosuu):  # すべての既存素数で割り切れなかったら素数
#         sosuu.append(L)

mx = 0
# print(sosuu)
for s in range(2, X):
    r = 2
    while s ** r <= X:
        # print('s: ', s, 'r: ', r, 's**r: ', s**r)
        mx = max(mx, s**r)
        r += 1
    # print('★ s**(r-1): ', s**(r-1), ' mx: ', mx, 's: ', s, 'r: ', r)


print(mx)
