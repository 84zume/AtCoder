N = int(input())
ans = 1

for i in range(1, N+1):
    ans *= i
    if ans > 10**9+7:
        ans %= 10**9+7

ans = ans % (10**9+7)

print(ans)
