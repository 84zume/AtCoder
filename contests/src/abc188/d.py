N, C = map(int, input().split())
abc = [list(map(int, input().split())) for i in range(N)]

# maxb = max(abc, key=lambda x: x[1])[1]+2

# print('maxb=', maxb)
# # いもす法で山を探す
# table = [0]*maxb
# for e in abc:
#     table[e[0]] += e[2]
#     table[e[1]+1] -= e[2]
#     print('e=', e)
#     # print('table=', table)

# # print('table=', table)
# for i in range(1, maxb):
#     table[i] += table[i-1]
# # print('table=', table)
# ans = 0

# for t in table:
#     if t > C:
#         ans += C
#     else:
#         ans += t
# print(ans)
