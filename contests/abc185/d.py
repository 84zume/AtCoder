import math

n, m = map(int, input().split())

if m == 0:
    print(1)
    exit(0)

a = list(map(int, input().split()))


if n == m:
    print(0)
    exit(0)

a = sorted(a)
sa = []


if a[0] == 1:
    minsa = n
else:
    minsa = a[0]-1
sa.append(a[0]-1)
for i in range(1, len(a)):
    s = a[i]-a[i-1]-1
    if s != 0:
        sa.append(s)
        minsa = min(minsa, s)
    #print(i, a[i-1], a[i],  minsa)

s = n-a[-1]
if s != 0:
    sa.append(s)
    minsa = min(minsa, s)

#print('sa', sa)
#print('minsa', minsa)

count = 0
for m in sa:
    count += math.ceil(m/minsa)
print(count)
