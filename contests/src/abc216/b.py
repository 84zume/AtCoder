N = int(input())
# ST = [list(map(str, input().split())) for i in range(N)]
ST = [input() for i in range(N)]

if len(ST) == len(set(ST)):
    print('No')
else:
    print('Yes')
