a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())

# if a == 0:
#     maxA = 0
# else:
#     maxA = x // a

# if b == 0:
#     maxB = 0
# else:
#     maxB = x // b

# if c == 0:
#     maxC = 0
# else:
#     maxC = x // c

cnt = 0
for ae in range(a+1):
    for be in range(b+1):
        for ce in range(c+1):
            if ae*500 + be*100 + ce*50 == x:
                cnt += 1
                #print(ae*500 + be*100 + ce*50)
                #print(ae, be, ce)
print(cnt)
