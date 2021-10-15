V, T, S, D = map(int, input().split())

if D < T*V or S*V < D:
    print('Yes')
else:
    print('No')
