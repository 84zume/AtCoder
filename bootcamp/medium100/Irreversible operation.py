S = input()
count = 0

# while S.count('BW') != 0:
#    count += S.count('BW')
#    S = S.replace('BW', 'WB')
place = 0
for i in range(len(S)):
    if S[i] == 'W':
        count += (i-place)
        place += 1

print(count)
