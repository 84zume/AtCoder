N, A, B = map(int, input().split())

sa = B-A

if sa % 2 == 0:
    print(sa//2)
else:
    hashi = min(A-1, N-B)
    print(hashi + 1 + (B-A-1)//2)
