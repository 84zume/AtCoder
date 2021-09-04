import re

N = str(input())

pattern = '\d9*'

if re.fullmatch(pattern, N):
    # print('match')
    print(int(N[0]) + (len(N)-1)*9)
else:
    # print('not match')
    print(int(N[0])-1 + (len(N)-1)*9)
