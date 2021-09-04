N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

l = [0]*N

l[0] = T[0]

for i in range(1, len(l)):
    l[i] = min(T[i], l[i-1]+S[i-1])

l[0] = min(l[0], l[N-1]+S[N-1])

for i in range(1, len(l)):
    l[i] = min(l[i], T[i], l[i-1]+S[i-1])

l[0] = min(l[0], l[N-1]+S[N-1])

for i in range(len(l)):
    print(l[i])
