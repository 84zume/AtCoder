from fractions import Fraction
N = int(input())

result = ''

while N != 0:
    if N == 1:
        N -= 1
        result += 'A'
    elif N % 2 == 1:
        N -= 1
        result += 'A'
    else:
        N = Fraction(str(N))/Fraction('2')
        result += 'B'

print(result[::-1])

# 検証
len = result[::-1]
ans = 0
for s in len:
    if s == 'A':
        ans += 1
    else:
        ans *= 2
print(ans)
