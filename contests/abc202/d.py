import itertools
A, B, K = map(int, input().split())

C = ''
for a in range(A):
    C += 'a'
for b in range(B):
    C += 'b'

# r = 0
# l = []
# while K > 2:
#     while K >= 2**r:
#         r += 1
#     l.append(r-1)
#     K -= 2**(r-1)
#     # print(K, r)
#     r = 0
# if K == 1:
#     l.append(K)

# print('l', l)

# pointer = A
# print(C)
# for e in l:
#     print(pointer - e, pointer)
#     C[pointer - e], C[pointer] = C[pointer], C[pointer - e]
#     pointer += 1
# print(''.join(C))
print(C)
for p in itertools.permutations(C):
    print(p)
# print(''.join(PC[K+1]))
#
