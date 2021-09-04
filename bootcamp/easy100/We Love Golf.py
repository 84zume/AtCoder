K = int(input())
A, B = map(int, input().split())

n = K

while n <= B:
    if A <= n and n <= B:
        print('OK')
        exit(0)
    n += K
print('NG')
