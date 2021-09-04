N = int(input())
P = list(map(int, input().split()))

Q = [0]*(N+1)

for i in range(len(P)):
    # print(P[i])
    Q[P[i]] = i+1

Q.pop(0)
print(*Q)
