s = str(input())
words = ['dream', 'dreamer', 'erase', 'eraser']

while(True):
    iscut = False
    for w in words:
        if s.endswith(w):
            s = s[:-len(w)]
            iscut = True
    if iscut == False:
        print('NO')
        break
    if len(s) == 0:
        print('YES')
        break
