# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
import math
X = [int(input()) for i in range(5)]

last_menu = 0
last_menu_minute = 10

for i in range(len(X)):
    if (X[i] % 10 != 0) and (last_menu_minute > (X[i] % 10)):
        last_menu_minute = X[i] % 10
        last_menu = i
last_menu_minute = X[last_menu]
del X[last_menu]

sumtime = 0
for x in X:
    sumtime += 10*math.ceil(x/10)

print(sumtime+last_menu_minute)
