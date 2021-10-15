N, X = map(int, input().split())
VP = [list(map(int, input().split())) for v in range(N)]
# print(VP)
al = 0
a = 0
for i in range(N):
    a = VP[i][0]*VP[i][1]
    al += a
    # print('a:', VP[i][0], VP[i][1], a, al)
    if al > X*100:
        print(i+1)
        exit(0)

print(-1)
