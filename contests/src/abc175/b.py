import itertools

N = int(input())
L = list(map(int, input().split()))
# L = set(L)
# print(L)
PL = []
c = 1
for l in L:
    PL.append([c, l])
    c += 1

cnt = 0
result = []
for hen in itertools.combinations(PL, 3):
    if(hen[0][1] + hen[1][1] > hen[2][1] and hen[0][1] + hen[2][1] > hen[1][1] and hen[1][1] + hen[2][1] > hen[0][1] and hen[0][1] != hen[1][1] and hen[1][1] != hen[2][1] and hen[0][1] != hen[2][1]):
        # print(hen)
        result.append(hen)
    # cnt += 1
# result = set(result)
print(len(result))
# print(result)
# print(cnt)
