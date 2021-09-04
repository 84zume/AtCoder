S = str(input())
K = int(input())
# 5000000000000000
# 1000000000000000000

if len(S) == 1:
    print(S[0])
else:
    for i in range(len(S)):
        if S[i] != '1' and i < K:
            print(S[i])
            exit(0)
    print(1)
