S = input()
T = input()

if len(T) - len(S) != 1:
    print('No')
    exit(0)

if S == T[:len(S)]:
    print('Yes')
else:
    print('No')
