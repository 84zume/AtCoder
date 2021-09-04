a, b = map(str, input().split())

suma = int(a[2]) + int(a[1]) + int(a[0])
sumb = int(b[2]) + int(b[1]) + int(b[0])

if suma >= sumb:
    print(suma)
else:
    print(sumb)
