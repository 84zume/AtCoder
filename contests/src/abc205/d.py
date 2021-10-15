N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = []
for i in range(Q):
    K.append([int(input()), i, 0])


K0 = sorted(K, key=lambda x: x[0])

counter = 1
ai = 0
bi = 1
ki = 0

while ki < len(K0):
    if counter == A[ai]:
        if ai < N-1:
            ai += 1
    else:
        if bi == K0[ki][0]:
            K0[ki][2] = counter
            ki += 1
        bi += 1
    counter += 1

K1 = sorted(K0, key=lambda x: x[1])

for k in K1:
    print(k[2])
