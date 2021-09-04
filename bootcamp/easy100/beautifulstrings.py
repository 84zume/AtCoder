from collections import Counter

w = str(input())
dic = Counter(w)

for d in dic.values():
    if(d % 2 == 1):
        print('No')
        exit(0)
print('Yes')
