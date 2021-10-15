N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

i_a = 0
i_b = 0
now_a = A[i_a]
now_b = B[i_b]
min_val = 9999999999

# print('now_a:', now_a)
# print('now_b:', now_b)
# i_a += 1
# i_b += 1
a_finised = False
b_finised = False

while True:
    # print('i_a', i_a, 'i_b', i_b)

    if a_finised == True:
        if i_b < M-1:
            now_b == B[i_b+1]
        else:
            now_b = B[i_b]
        min_val = min(min_val, abs(now_a-now_b))
        break
    elif b_finised == True:
        if i_a < N-1:
            now_a = A[i_a+1]
        else:
            now_a = A[i_a]
        min_val = min(min_val, abs(now_a-now_b))
        break
    else:
        if A[i_a] < B[i_b]:
            now_a = A[i_a]
            # print('now_a:', now_a)
            i_a += 1
            if i_a > N-1:
                a_finised = True
        elif B[i_b] < A[i_a]:
            now_b = B[i_b]
            # print('now_b:', now_b)
            i_b += 1
            if i_b > M-1:
                b_finised = True
        else:
            print(0)
            exit(0)

    # print('★', now_a, now_b)
    min_val = min(min_val, abs(now_a-now_b))

    # if a_finised or b_finised:
print(min_val)
