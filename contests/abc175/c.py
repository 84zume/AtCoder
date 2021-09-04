import math
import sys
x, k, d = map(int, input().split())

l = math.floor(x / d)
if(l >= k):
    x -= k*d
    print(abs(x))
    sys.exit()
else:
    x -= l*d
k = k-l

if(k % 2 == 0):
    print(abs(x))
else:
    print(abs(x-d))

# while i < k:
#     if(x >= 0):
#         x -= d
#     else:
#         x += d
#     #     isReturn = True

#     # if isReturn:
#     #     if((k-i) % 2 == 0):
#     #         i = k-2
#     #     else:
#     #         i = k-1

#     i += 1

# print(abs(x))
