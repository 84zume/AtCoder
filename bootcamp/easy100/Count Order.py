import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

list_n = []

for n in range(1, N+1):
    list_n.append(n)

all_comb_n = itertools.permutations(list_n)

cnt = 1
at_P = 0
at_Q = 0
for i in all_comb_n:
    if(i == P):
        at_P = cnt
    if(i == Q):
        at_Q = cnt
    cnt = cnt + 1

print(abs(at_P-at_Q))
#p_at = all_comb_n.index(P)
# print(all_comb_n)
