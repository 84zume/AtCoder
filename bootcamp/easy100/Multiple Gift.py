X, Y = map(int, input().split())

ans = X
cnt = 1

while ans <= Y:
    ans *= 2
    cnt += 1

print(cnt - 1)
