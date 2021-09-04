N = int(input())
B = list(map(int, input().split()))


# ZB = [B[0]] + B + [B[-1], B[-1]]
# # print(ZB)

# A = []
# # j = 0
# for i in range(1, len(ZB)-1):
#     # print(i)
#     A.append(min(ZB[i-1], ZB[i], ZB[i+1]))
#     # j += 1
# print(sum(A))

A = [0] * N
ZB = [B[0]] + B + [B[-1]]

for i in reversed(range(0, N)):
    A[i] = min(ZB[i], ZB[i+1])
print(sum(A))
