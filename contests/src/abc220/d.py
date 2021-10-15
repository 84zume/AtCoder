N = int(input())
A = list(map(int, input().split()))

temp = [[0] * 10 for i in range(N-1)]

n1 = A.pop(0)
n2 = A.pop(0)
depth = 0

F = (n1 + n2) % 10
G = (n1 * n2) % 10

temp[depth][F] += 1
temp[depth][G] += 1

# print(temp)

while len(A) > 0:
    val = A.pop(0)
    depth += 1
    for n_idx in range(10):
        if temp[depth-1][n_idx] != 0:
            F = (n_idx + val) % 10
            G = (n_idx * val) % 10
            # print('depth', depth, 'val', n_idx, val, '=>', 'F', F, '/ G', G)
            temp[depth][F] += (temp[depth-1][n_idx] % 998244353)
            temp[depth][G] += (temp[depth-1][n_idx] % 998244353)
            # print('前', temp[depth-1])
            # print('今', temp[depth])
            # print('')

# top = temp[-1].pop(0)
# temp[-1].append(top)
for t in temp[-1]:
    print(t % 998244353)
