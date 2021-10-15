n = str(input())

b = n

while True:
    a = b[::-1]

    if b == a:
        print('Yes')
        exit(0)

    if len(b) > 20:
        break

    b = '0' + b

print('No')
# 00000000100000000
