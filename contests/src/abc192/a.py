X = int(input())

# i = int(X/100)
# f = X/100 - i
# print(f, i)
# if i % 100 == 0 and i != 0:
#     print(100)
# else:
#     print(int(100 - f*100))

if X % 100 == 0:
    print(100)
    exit(0)

while X > 100:
    X -= 100
print(100-X)
