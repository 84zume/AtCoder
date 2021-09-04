X = input()


def func_next(n):
    if n == 9:
        return 0
    else:
        return n+1


if X[0] == X[1] and X[0] == X[2] and X[0] == X[3]:
    print('Weak')
    exit(0)

w_flag = True
for i in range(3):
    if int(X[i+1]) != func_next(int(X[i])):
        w_flag = False


if w_flag:
    print('Weak')
else:
    print('Strong')
