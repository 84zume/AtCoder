import math


def checkKaibun(l):
    a = ''.join(l)
    b = ''.join(list(reversed(l)))
    if a == b:
        return True
    else:
        return False


def listreplace(L, f, t):
    strL = '.' + '..'.join(L) + '.'
    f1 = '.' + f+'.'
    t1 = '.' + t+'.'
    r = strL.replace(f1, t1)
    r = r.replace('.', ' ')
    return r.split()


N = int(input())
A = list(map(str, input().split()))

cnt = 0
if checkKaibun(A):
    print(cnt)
    exit(0)

for i in range(math.floor(N/2)):
    # print(i, 'check: ', A[i], A[N-i-1])
    if A[i] != A[N-i-1]:
        A = listreplace(A, A[N-i-1], A[i])
        # print(i, A, cnt)
        cnt += 1
    if checkKaibun(A):
        print(cnt)
        exit(0)
