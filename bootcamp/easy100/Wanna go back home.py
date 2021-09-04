S = str(input())

if S.find('N') >= 0 and S.find('S') == -1:
    print('No')
    exit(0)

if S.find('S') >= 0 and S.find('N') == -1:
    print('No')
    exit(0)

if S.find('W') >= 0 and S.find('E') == -1:
    print('No')
    exit(0)

if S.find('E') >= 0 and S.find('W') == -1:
    print('No')
    exit(0)

print('Yes')
