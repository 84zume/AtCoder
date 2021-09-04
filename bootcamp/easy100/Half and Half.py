# A, B, C(AB) ピザの値段
# AがX枚, BがY枚のピザが欲しい
# いくらか
import math

A, B, C, X, Y = map(int, input().split())

A_half = C/2
B_half = C/2

CountA = 0
CountB = 0
CountC = 0
# ハーフを優先して買う

if (A+B)/4 >= A_half:
    if X >= Y:
        CountC += 2*Y
        if A >= 2*C:
            CountC += 2*(X-Y)
        else:
            CountA += X-Y
    else:
        CountC += 2*X
        if B >= 2*C:
            CountC += 2*(Y-X)
        else:
            CountB += Y-X
else:
    CountA += X
    CountB += Y

# print('half: ', A_half, 'Ave.:', (A+B)/4)
# print('CountA:', CountA, 'CountB: ', CountB, 'CountC: ', CountC)
print(CountA*A + CountB*B + CountC*C)
