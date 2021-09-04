S = input()
l = [0]*(len(S)+1)
for i in range(len(S)):
    if S[i] == '<':
        l[i+1] = l[i] + 1
    elif S[i] == '>':
        l[i+1] = min(l)  # l[i] - 1
minl = min(l)
if minl < 0:
    for i in range(len(l)):
        l[i] += abs(minl)


if(S[0] == '<'):
    l[0] = 0
if(S[-1] == '>'):
    l[-1] = 0

ans = []
for i in range(len(S)):
    ans.append(l[i])
    ans.append(S[i])
ans.append(l[-1])
print(ans)


print(sum(l))
