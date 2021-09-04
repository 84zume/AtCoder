N = int(input())
a = [int(input()) for i in range(N)]

count = 1
i = 0
while a[i] != 2:
    i = a[i] - 1
    count += 1
    if count == N:
        print(-1)
        exit(0)

print(count)
