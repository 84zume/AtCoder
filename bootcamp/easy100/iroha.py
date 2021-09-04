# Lは文字列の長さ
N, L = map(int, input().split())
S = [str(input()) for i in range(N)]

SortedS = sorted(S)
print(''.join(SortedS))
