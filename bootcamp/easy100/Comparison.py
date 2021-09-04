A = str(input())
B = str(input())

if A == B:
    print('EQUAL')


if len(A) > len(B):
    print('GREATER')
elif len(B) > len(A):
    print('LESS')
else:
    for i in range(len(A)):
        if A[i] > B[i]:
            print('GREATER')
            exit(0)
        elif B[i] > A[i]:
            print('LESS')
            exit(0)
