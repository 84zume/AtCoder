S = str(input())

if S[0] != 'A':
    print('WA')
    exit(0)

head = S[2:]
tail = head[:-1]
# print(tail)
if tail.count('C') != 1:
    print('WA')
    exit(0)

nokori = tail.replace('A', '').replace('C', '')

if S[1].islower() and S[-1].islower() and (nokori.islower() or nokori == ''):
    print('AC')
else:
    print('WA')
