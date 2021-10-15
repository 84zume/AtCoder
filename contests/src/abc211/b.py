s = []
c = ['2B', '3B', 'H', 'HR']
for i in range(4):
    s.append(input())

s = sorted(s)

for i in range(4):
    if s[i] != c[i]:
        print('No')
        exit(0)
print('Yes')
