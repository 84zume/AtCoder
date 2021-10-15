N = int(input())
A = list(map(int, input().split()))

cnt = 0
for n in A:
    if n > 10:
        cnt += (n - 10)
print(cnt)
