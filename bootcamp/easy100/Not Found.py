s = str(input())

unique_s = ''.join(sorted(set(s)))
# print(unique_s)

for i in range(97, 123):
    if unique_s.count(chr(i)) == 0:
        print(chr(i))
        exit(0)
print('None')
