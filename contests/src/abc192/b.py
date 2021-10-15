S = str(input())

ans = True
i = 0

for i in range(len(S)):
    if i % 2 == 1:
        if S[i].islower():
            print('No')
            exit(0)
    else:
        if S[i].isupper():
            print('No')
            exit(0)
print('Yes')
