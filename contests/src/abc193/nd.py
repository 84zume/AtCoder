# 9K枚のカードがある
# 高橋君4表、1裏→S、青木君4表、1裏→T
# 先頭4文字は1～9, #

def cal(a):
    ans = 0
    # print('a', a)
    for i in range(1, 10):
        # if a.count(str(i)) > 0:
        # print('途中 ', i * 10**a.count(str(i)))
        ans += i * 10**a.count(str(i))
    # print('ans', ans)
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
# print(deck)
zanDeck = sum(deck)
for i in range(9):
    if deck[i] > 0:
        PossibleS.append([S[0], S[1], S[2], S[3], i+1, deck[i] /
                          zanDeck, cal([S[0], S[1], S[2], S[3], str(i+1)])])
        PossibleT.append([T[0], T[1], T[2], T[3], i+1, deck[i] /
                          zanDeck, cal([T[0], T[1], T[2], T[3], str(i+1)])])

ps = 0
for s in PossibleS:
    for t in PossibleT:
        if s[6] > t[6]:
            ps += s[5]*(deck[t[4]]/(zanDeck-1))
            print('S', s[6], 'T', t[6], t[4], deck[t[4]])

print(ps)

# for p in PossibleS:
#     print('S', p)

# for p in PossibleT:
#     print('T', p)
