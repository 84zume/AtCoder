N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

sortedAB = sorted(AB, key=lambda x: x[0])

count = 0
money = 0
omise = 0
while count < M:
    count += 1
    money += sortedAB[omise][0]
    sortedAB[omise][1] -= 1
    if sortedAB[omise][1] == 0:
        omise += 1
print(money)
