def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


X = input()

dot = my_index(X, '.', -1)

if dot == -1:
    print(X)
else:
    print(X[:dot])
