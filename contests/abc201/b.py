# N = int(input())
# S = []
# T = []
# for i in range(N):
#     s, t = input().split()
#     S.append(s)
#     T.append(t)

# t1 = sorted(T)
# idx = T.index(t1[-2])
# print(S[idx])


N = int(input())
ST = []
for i in range(N):
    s, t = input().split()
    ST.append([s, int(t)])

ST.sort(key=lambda x: x[1])
print(ST[-2][0])
