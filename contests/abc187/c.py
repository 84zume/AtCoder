N = int(input())
S = [str(input()) for i in range(N)]

S_unique = list(set(S))
# print(S_unique)
SS = []
for s in S_unique:
    if s[0] == '!':
        SS.append(s[1:] + '!')
    else:
        SS.append(s)
SS.sort()
# print(SS)

idx = 0
for i in range(1, len(SS)):
    if SS[idx] + '!' == SS[i]:
        print(SS[idx])
        exit(0)
    idx += 1
print('satisfiable')
