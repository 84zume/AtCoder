O = str(input())
E = str(input())

ans = ''

for i in range(len(E)):
    ans += O[i]
    ans += E[i]

if len(O) - len(E) == 1:
    ans += O[-1]

print(ans)
