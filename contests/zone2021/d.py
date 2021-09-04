S = input()

T = ''
R = 0
for i in range(len(S)):
    s = S[i]
    if(s == 'R'):
        if R == 0:
            R = 1
        else:
            R = 0
    else:
        if R == 0:
            if len(T) > 0:
                if T[-1] == s:
                    T = T[:-1]
                else:
                    T += s
            else:
                T = s
        else:
            if len(T) > 0:
                if s == T[0]:
                    T = T[1:]
                else:
                    T = s + T
            else:
                T = s
if R == 1:
    print(T[::-1])
else:
    print(T)
