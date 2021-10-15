N = int(input())
T = list(map(int, input().split()))

T2 = sorted(T, reverse=True)

a = [T2[0]]

if N == 1:
    print(sum(a))
    exit(0)

b = [T2[1]]

if N == 2:
    print(max(sum(a), sum(b)))
    exit(0)

for i in range(2, len(T)):
    if sum(a) > sum(b):
        b.append(T2[i])
    else:
        a.append(T2[i])

print(max(sum(a), sum(b)))
