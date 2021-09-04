n, k = map(int, input().split())
p = list(map(int, input().split()))

p = sorted(p)  # 小さい順
sum = 0

for i in range(k):
    sum += p[i]
print(sum)
