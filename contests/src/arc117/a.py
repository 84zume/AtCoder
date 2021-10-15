a, b = map(int, input().split())

list_a = []
list_b = []


if a >= b:
    for i in range(a):
        list_a.append(i+1)
    sum_a = sum(list_a)

    for i in range(b-1):
        list_b.append(-(i+1))
    list_b.append(-(sum_a + sum(list_b)))
else:
    for i in range(b):
        list_b.append(-(i+1))
    sum_b = sum(list_b)

    for i in range(a-1):
        list_a.append(i+1)
    list_a.append(-(sum_b + sum(list_a)))


print(" ".join(map(str, list_a+list_b)))
# print(sum(list_a)+sum(list_b))
