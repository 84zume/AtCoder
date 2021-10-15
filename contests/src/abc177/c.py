import itertools

N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
# sum = 0

# for pair in itertools.combinations(A, 2):
#     # print(pair)
#     sum += pair[0] * pair[1]
#     if(sum >= 10**9+7):
#         sum = sum % (10**9+7)

# print(sum % (10**9+7))

B = [0]

for i in range(N):
    B.append(B[i] + A[i])

ans = 0

for i in range(N):
    sum = (B[N] - B[i+1]) % mod
    ans += A[i] * sum
    ans %= mod
print(ans)
