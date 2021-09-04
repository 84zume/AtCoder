N, W = map(int, input().split())

cnt = 0

while W*cnt <= N:
    cnt += 1

print(cnt-1)
