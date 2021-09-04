N = int(input())
SP = []
# P = []

for i in range(N):
    s, p = input().split()
    SP.append([str(s), int(p), i+1])
    # P.append(int(p))

SortedSP1 = sorted(SP, key=lambda x: (x[1]), reverse=True)
SortedSP2 = sorted(SortedSP1, key=lambda x: (x[0]), reverse=False)

for e in SortedSP2:
    print(e[2])
