import math
n = int(input())

round_n = math.ceil(n/1000)*1000

print(round_n-n)
