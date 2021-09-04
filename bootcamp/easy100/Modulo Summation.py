N = int(input())
a = list(map(int, input().split()))

# mod_maxA = 2 * max(a)

# maxf = 0
# for m in range(2, mod_maxA):
#     temp = 0
#     for e in a:
#         temp += (m % e)
#         print('-', m, m % e)
#     print(temp, maxf)
#     maxf = max(temp, maxf)

# print(maxf)

ans = 0
for e in a:
    ans += (e-1)
print(ans)
