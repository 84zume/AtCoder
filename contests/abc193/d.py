# 9K枚のカードがある
# 高橋君4表、1裏→S、青木君4表、1裏→T
# 先頭4文字は1～9, #

def cal(a):
    ans = 0
    for i in range(1, 10):
        ans += i * 10**a.count(str(i))
    return ans


K = int(input())
S = str(input())
T = str(input())


deck = [K] * 9

for i in range(4):
    deck[int(S[i])-1] -= 1
    deck[int(T[i])-1] -= 1

PossibleS = []
PossibleT = []
zanDeck = sum(deck)
print(deck)
for i in range(9):
    if deck[i] > 0:
        s = [S[0], S[1], S[2], S[3], str(i+1)]
        s.append(deck[i]/zanDeck)
        s.append(cal(s))
        t = [T[0], T[1], T[2], T[3], str(i+1)]
        t.append(deck[i]/zanDeck)
        t.append(cal(t))
        PossibleS.append(s)
        PossibleT.append(t)

loseCount = 0
winCount = 0
for s in PossibleS:
    for t in PossibleT:
        if s[6] > t[6]:
            loseCount += 1
        else:
            winCount += 1
# print(s[5]*ps/(zanDeck-1))
print(winCount/(loseCount+winCount))

# for p in PossibleS:
#     print('S', p)

# for p in PossibleT:
#     print('T', p)
