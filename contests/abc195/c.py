import math


def SumComma(rui):
    kazu = [
        [0, 0],
        [1, 0],
        [2, 0],
        [3,    10**4-10**3],
        [4,    10**5-10**4],
        [5,    10**6-10**5],
        [6, 2*(10**7-10**6)],
        [7, 2*(10**8-10**7)],
        [8, 2*(10**9-10**8)],
        [9, 3*(10**10-10**9)],
        [10, 3*(10**11-10**10)],
        [11, 3*(10**12-10**11)],
        [12, 4*(10**13-10**12)],
        [13, 4*(10**14-10**13)],
        [14, 4*(10**15-10**14)]
    ]

    ans = 0

    for i in range(rui+1):
        ans += kazu[i][1]
    return ans


def ketaComma(rui):
    kazu = [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 1],
        [4, 1],
        [5, 1],
        [6, 2],
        [7, 2],
        [8, 2],
        [9, 3],
        [10, 3],
        [11, 3],
        [12, 4],
        [13, 4],
        [14, 4],
        [15, 5]
    ]
    return kazu[rui][1]


N = int(input())

# なに累乗か
rui = math.log10(N)
min_rui = math.floor(rui)
# print(min_rui)
s = SumComma(min_rui-1)
# print(s)
keta = ketaComma(min_rui)
sa = N - 10**min_rui+1
print(s + keta*sa)
