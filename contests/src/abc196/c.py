import math
N = int(input())

maxKeta = math.floor((len(str(N)))/2)
count = 0

# print(maxKeta)
for i in range(1, (10 ** maxKeta)+1):
    if int(str(i) + str(i)) <= N:
        # print(int(str(i) + str(i)))
        count += 1
print(count)
