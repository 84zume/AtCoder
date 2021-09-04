N = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(len(a)):
    if(i+1 == a[a[i]-1]):
        count += 1
print(int(count/2))
