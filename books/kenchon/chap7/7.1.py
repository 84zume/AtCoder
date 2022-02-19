# N = int(input())
A = [1,2,3,4,5]
B = [4, 3, 5, 7]

A = sorted(A)
B = sorted(B)

# A = sorted(list(map(int, input())))
# B = sorted(list(map(int, input())))

count = 0
for a in A:
    for b in B:
        if a < b:
            count += 1
            break
print(count)
