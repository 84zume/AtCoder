N, M = map(int, input().split())
PS = [list(map(str, input().split())) for i in range(M)]

SortedPS = sorted(PS, key=lambda x: x[0])

i = 0
countAC = 0
countWA = 0
while i < M:
    problem = SortedPS[i][0]
    j = i
    tempCountWA = 0
    # print('problem: ', problem)
    while j < M and SortedPS[j][0] == problem and SortedPS[j][1] == 'WA':
        j += 1
        tempCountWA += 1
        # if j >= M:
        #     break
    # print('j: ', j, 'countWA:', countWA, 'SortedPS[j][1]:', SortedPS[j][1])

    if j < M and SortedPS[j][0] == problem and SortedPS[j][1] == 'AC':
        countAC += 1
        countWA += tempCountWA

    while j < M and SortedPS[j][0] == problem:
        j += 1
        # if j >= M:
        #     break
    i = j

print(countAC, countWA)
