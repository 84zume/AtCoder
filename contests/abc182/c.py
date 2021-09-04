import itertools
N = str(input())

for l in reversed(range(len(N)+1)):
    # 並べ替えは関係ない前提
    targets = itertools.combinations(N, l)
    for t in targets:
        if(len(t) == 0):
            print(-1)
            exit(0)
        # print(t)
        summ = 0
        for e in t:
            summ += int(e)
        # print(summ)
        if(summ % 3 == 0):
            # print("good")
            print(len(N)-l)
            exit(0)
