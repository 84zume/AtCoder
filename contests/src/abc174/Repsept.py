def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


k = int(input())

num = 7
cnt = 1
if k % 2 == 0:
    print(-1)
elif k % 5 == 0:
    print(-1)
# elif is_prime(k) and k >= 19:
#     print(k-1)
else:
    while True:
        if num % k == 0:
            break
        cnt += 1
        num = int(str(num) + '7')
    print(cnt)
