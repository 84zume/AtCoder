N = int(input())

ans = 0
day = 1

while ans < N:
    ans += day
    day += 1

print(day-1)
