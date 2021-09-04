n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

non_dupli = set(d)
print(len(non_dupli))
