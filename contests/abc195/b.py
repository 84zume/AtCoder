import math
# Aグラム以上、Bグラム以下、合計Wキログラム
A, B, W = map(int, input().split())

minVal = math.ceil(W*1000 / B)
maxVal = math.floor(W*1000 / A)

if(minVal <= maxVal):
    print(minVal, maxVal)
else:
    print('UNSATISFIABLE')
