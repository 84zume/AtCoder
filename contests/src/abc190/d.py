import math
N = int(input())

if N == 1:
    print(2)
    exit(0)

t = math.ceil(N**0.5)


cnt = 0
for i in range(1, t):
    if N % i == 0:
        if i % 2 == 1 and (N/i) % 2 == 0:
            cnt += 1
        elif i % 2 == 0 and (N/i) % 2 == 1:
            cnt += 1
print(cnt * 2)
