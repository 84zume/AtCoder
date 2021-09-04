import itertools

s1 = str(input())
s2 = str(input())
s3 = str(input())

all = s1 + s2 + s3
nashi = list(set(all))

kazu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
v = itertools.permutations(kazu, len(nashi))

for e in v:
    for i in range(len(nashi)):
        # print(nashi[i], e[i])
        s1 = s1.replace(nashi[i], str(e[i]))
        s2 = s2.replace(nashi[i], str(e[i]))
        s3 = s3.replace(nashi[i], str(e[i]))
    # print(s1, s2, s3)
    if int(s1) + int(s2) == int(s3):
        print(s1)
        print(s2)
        print(s3)
        exit(0)
print('UNSOLVABLE')
