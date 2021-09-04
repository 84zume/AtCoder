N, W = map(int, input().split())
S = []
T = []
P = []
for i in range(N):
    s, t, p = map(int, input().split())
    S.append(s)
    T.append(t)
    P.append(p)

use_list = [0] * (max(T)+1)

for i in range(N):
    #    print(i)
    use_list[S[i]] += P[i]
    use_list[T[i]] -= P[i]
#    print(i, use_list)

for i in range(len(use_list)):
    if 0 < i:
        use_list[i] += use_list[i-1]

max_value = max(use_list)
# print(max_value)

if max_value <= W:
    print('Yes')
else:
    print('No')
