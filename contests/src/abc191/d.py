import math
X, Y, R = map(float, input().split())

startX = math.ceil(X-R)
endX = math.floor(X+R)
print('startX:', startX, ', endX:', endX)
cnt = 0

for i in range(startX, endX+1):
    henX = abs(X-i)
    henY = (R**2 - henX**2)**0.5
    henY_count = math.floor(henY * 2)
    if henY == 0:
        henY_count += 1
    elif henX == 0:
        henY_count += 1
    elif math.ceil(henY) == henY:
        henY_count += 2
    cnt += henY_count
    # print('henX: ', henX, ', henY: ', henY, ', henY_count:', henY_count)
print(cnt)
