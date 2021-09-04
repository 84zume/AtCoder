N, X = map(int, input().split())
S = str(input())

for s in S:
    if(s == 'x' and X > 0):
        X -= 1
    elif(s == 'o'):
        X += 1
print(X)
