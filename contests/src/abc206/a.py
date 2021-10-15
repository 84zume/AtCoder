import math
n = int(input())

cost = math.floor(n * 1.08)

if cost < 206:
    print('Yay!')
elif cost == 206:
    print('so-so')
else:
    print(':(')
