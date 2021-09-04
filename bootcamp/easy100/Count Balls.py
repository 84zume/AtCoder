N, A, B = map(int, input().split())

sho = N // (A+B)
ama = N % (A+B)

blue = sho * A

if(ama < A):
    blue = blue + ama
else:
    blue = blue + A

print(blue)
