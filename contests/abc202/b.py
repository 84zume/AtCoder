s = str(input())

r = s[::-1]
a = ''
for e in r:
    if e == '6':
        a += '9'
    elif e == '9':
        a += '6'
    else:
        a += e

print(a)
