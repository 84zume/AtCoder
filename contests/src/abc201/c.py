S = input()
# S = 'ooo???xxxx'
cnt = 0
for i in range(10000):
    t = S
    c = ['n']*10
    n = str(i).zfill(4)
    # print(n)
    for e in n:
        # print('*', e)
        if t[int(e)] == 'x':
            c[int(e)] = 'z'
        elif t[int(e)] == 'o':
            c[int(e)] = 'o'
        else:
            c[int(e)] = 'o'
    check = True
    # print('c', c)
    for i in range(10):
        if (t[i] == 'o' and (c[i] == '?' or c[i] == 'x' or c[i] == 'n')):
            check = False
        if c[i] == 'z':
            check = False
    if check:
        cnt += 1
        # print('c', c)
        # print(n)
print(cnt)
