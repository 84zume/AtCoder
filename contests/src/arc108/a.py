import math

s, p = map(int, input().split())

x = s**2 - 4*p
# print(x)
y = math.floor(math.sqrt(x)) ** 2
# print(y)
if x == y:
    print('Yes')
else:
    print('No')


# if math.sqrt(x).is_integer():
#     print(math.sqrt(x))
#     print('Yes')
# else:
#     print('No')
