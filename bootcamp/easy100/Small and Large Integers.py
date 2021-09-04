A, B, K = map(int, input().split())

ans = []

for i in range(A, A+K):
    if A <= i and i <= B:
        ans.append(i)

for i in range(B-K+1, B+1):
    if A <= i and i <= B:
        ans.append(i)

anslist = list(set(ans))

for i in anslist:
    print(i)
