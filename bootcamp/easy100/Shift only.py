N = int(input())
A = list(map(int, input().split()))


def count2(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt


result = 100000
for n in A:
    result = min([result, count2(n)])
print(result)
