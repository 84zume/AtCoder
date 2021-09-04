H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

minA = 100
for la in A:
    for a in la:
        minA = min(minA, int(a))


count = 0

for la in A:
    for a in la:
        count += (int(a) - minA)
print(count)
