n = int(input())
t0 = 0
x0 = 0
y0 = 0
count = 0
for i in range(n):
    t, x, y = map(int, input().split())
    kyori = abs(x - x0) + abs(y - y0)
    zikoku = abs(t-t0)
    t0 = t
    x0 = x
    y0 = y

    if kyori > zikoku or kyori % 2 != zikoku % 2:
        count = count+1
    else:
        count = 0

if count == 0:
    print("Yes")
else:
    print("No")
