import math
N = int(input())
maxN = math.ceil(N**0.5)
for i in reversed(range(maxN+1)):
    if N % i == 0:
        break
# print(i)
# print(maxN)
print((i-1)+(N//i-1))
