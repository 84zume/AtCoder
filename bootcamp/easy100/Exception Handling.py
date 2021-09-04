import copy
N = int(input())
A = [int(input()) for i in range(N)]

top1 = sorted(A)[-1]
top2 = sorted(A)[-2]
# print(top1, top2)
for i in A:
    # print("oo", i)
    if i == top1:
        print(top2)
    else:
        print(top1)
