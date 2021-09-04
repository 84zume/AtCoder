a, b = map(int, input().split())
s = str(input())

if s.count('-') != 1:
    print('No')
    exit(0)

s1, s2 = s.split('-')

if len(s1) == a and len(s2) == b:
    print('Yes')
else:
    print('No')
