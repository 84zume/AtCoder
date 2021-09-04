s = str(input())


if len(s) % 2 == 0:
    pa = ['0', '1'] * int(len(s)/2)
    pb = ['1', '0'] * int(len(s)/2)
else:
    pa = ['0', '1'] * (len(s)//2)
    pa.append('0')
    pb = ['1', '0'] * (len(s)//2)
    pb.append('1')

cnta = 0
cntb = 0

for i in range(len(s)):
    # print(s[i], pa[i], pb[i])
    if s[i] != pa[i]:
        cnta += 1
    if s[i] != pb[i]:
        cntb += 1

print(min(cnta, cntb))
