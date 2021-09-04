D, N = map(int, input().split())
# 100でちょうどD回割り切れる正の整数

if N == 100:
    if D == 0:
        print(101)
    elif D == 1:
        print(100*(N+1))
    elif D == 2:
        print(100*100*(N+1))
else:
    if D == 0:
        print(N)
    elif D == 1:
        print(100*N)
    elif D == 2:
        print(100*100*N)
