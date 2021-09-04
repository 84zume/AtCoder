S = str(input())
T = str(input())

for i in range(len(T)):
    if S == T:
        print('Yes')
        exit(0)
    T = T[1:] + T[0]
print('No')
