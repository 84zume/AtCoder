import numpy as np
n = int(input())
a = list(map(int, input().split()))

# x = 0
# maxx = 0
# for i in range(n+1):
#     for e in range(i):
#         x += a[e]
#         #print(a[e], x)
#         maxx = max(x, maxx)
# print(maxx)

l = np.array(a)
result = np.cumsum(l)
result2 = np.cumsum(result)
print(result2)
