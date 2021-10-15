N, X = map(int, input().split())
A = list(map(str, input().split()))
strX = str(X)
newA = [e for e in A if e != strX]
strA = ' '.join(newA)
print(strA)
