a, b, c, d = map(int, input().split())

cnt = 0
c1 = 0

while True:
    if a <= c1 * d:
        print(cnt)
        exit(0)
    cnt += 1
    a += b
    c1 += c
    if cnt > 1000000:
        print(-1)
        exit(0)
