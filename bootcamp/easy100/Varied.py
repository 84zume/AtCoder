s = str(input())

s_uniquie = ''.join(set(s))

if(len(s) == len(s_uniquie)):
    print('yes')
else:
    print('no')
