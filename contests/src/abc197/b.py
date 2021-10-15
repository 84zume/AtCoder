import collections
H, W, X, Y = map(int, input().split())
S = [input() for i in range(H)]

shita = 0
ue = 0
migi = 0
hidari = 0
result = []
# y↓
i = 0
count = 0
while Y - 1 + i < W and S[X - 1][Y-1 + i] != '#':
    # print([X - 1, Y-1 + i])
    result.append([X - 1, Y-1 + i])
    i += 1
    count += 1
migi = Y-1 + i
# print(count)

# y↑
i = 0
while Y - 1 + i >= 0 and S[X - 1][Y-1 + i] != '#':
    # print([X - 1, Y-1 + i])
    result.append([X - 1, Y-1 + i])
    i -= 1
    count += 1
hidari = Y-1 + i
# print(count)

# x→
j = 0
while X-1 + j < H and S[X - 1 + j][Y-1] != '#':
    # print([X - 1 + j, Y-1])
    result.append([X - 1 + j, Y-1])
    j += 1
    count += 1
shita = X - 1 + j
# print(count)

# y↑
j = 0
while X-1 + j >= 0 and S[X - 1 + j][Y-1] != '#':
    # print([X - 1 + j, Y-1])
    result.append([X - 1 + j, Y-1])
    j -= 1
    count += 1
ue = X - 1 + j
# print(shita, ue, migi, hidari)
print(count-3)
