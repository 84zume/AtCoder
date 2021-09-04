N = int(input())
x = list(map(int, input().split()))

m = 0
u = 0
c = 0

for e in x:
    m += abs(e)
    u += e**2
    c = max(c, abs(e))

print(m)
print(u**0.5)
print(c)
