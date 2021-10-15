import math
t, N = map(int, input().split())

val = 1/(t/100)

print(math.ceil(N*val+N-1))
