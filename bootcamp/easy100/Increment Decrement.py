n = int(input())
s = str(input())

x = 0
max_x = x
for e in s:
    if e == "I":
        x += 1
    if e == "D":
        x -= 1
    max_x = max(max_x, x)
print(max_x)
