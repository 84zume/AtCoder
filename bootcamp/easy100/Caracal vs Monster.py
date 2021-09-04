H = int(input())

cnt = 0

while H > 1:
    H = H // 2
    cnt = cnt + 1

node = 0
for n in range(cnt+1):
    node = node + 2 ** n

print(node)
