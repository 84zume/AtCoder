N = int(input())
H = list(map(int, input().split()))

# tancho = True
H[0] -= 1
for i in range(1, N):
    # print(H)
    if H[i] < H[i-1]:
        print('No')
        exit(0)

    if H[i] > H[i-1]:
        H[i] -= 1
print('Yes')
