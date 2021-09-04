N = int(input())
a = list(map(int, input().split()))

# mid_a = sorted(a)[N:2*N]

# print(sum(mid_a))
sorted_s = sorted(a, reverse=True)

# i = 0
# ans = 0
# while i+2 < 3*N:
#     # print(sorted_s[i+1])
#     ans += sorted_s[i+1]
#     i += 3
# print(ans)
i = 0
ans = 0
while i < 2*N:
    ans += sorted_s[i+1]
    i += 2

print(ans)
