S = str(input())
T = str(input())

ans = len(T)

for start in range(len(S)-len(T)):
    diff = 0
    for i in range(len(T)):
        if(T[i] != S[start+i]):
            diff += 1
    ans = min(ans, diff)
print(ans)
