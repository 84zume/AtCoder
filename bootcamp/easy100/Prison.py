n, m = map(int, input().split())
x = [list(map(int, input().split())) for i in range(m)]
L = []
R = []

for e in x:
    L.append(e[0])
    R.append(e[1])


maxL = max(L)
maxR = min(R)
# print(maxL)
# print(maxR)
if (maxR-maxL+1) < 0:
    print(0)
else:
    print(maxR-maxL+1)
