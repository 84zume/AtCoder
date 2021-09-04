import itertools

S = str(input())
A = (int)(S[0])
B = (int)(S[1])
C = (int)(S[2])
D = (int)(S[3])

oplist = []
for p1 in ['+', '-']:
    for p2 in ['+', '-']:
        for p3 in ['+', '-']:
            oplist.append([p1, p2, p3])


# oplist = itertools.combinations(['+', '-'], 3)

formula = ''

for op in oplist:
    # print(op)
    ans = 0
    if op[0] == '+':
        ans += (A+B)
    else:
        ans += (A-B)

    if op[1] == '+':
        ans += C
    else:
        ans -= C

    if op[2] == '+':
        ans += D
    else:
        ans -= D

    if ans == 7:
        formula = (str)(A)+op[0]+str(B)+op[1]+str(C)+op[2]+str(D) + '=7'
        print(formula)
        break
