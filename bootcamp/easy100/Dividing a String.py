S = str(input())

a = S[0]
b = ''
cnt = 1

i = 1
j = 0
# ans = a
while i+j+1 <= len(S):
    b = S[i:i+j+1]
    if a != b:
        cnt += 1
        i = i + j + 1
        j = 0
        a = b
        # ans += " "
        # ans += a
    else:
        j += 1
print(cnt)
# print(ans)
