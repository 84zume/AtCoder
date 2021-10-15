a, b, c = map(int, input().split())

cnt = 0
kitai = 0
while a <= 100 or b <= 100 or c <= 100:
    kitai = 2*a/(a+b+c) + 2*b/(a+b+c) + 2*c/(a+b+c)
    a += kitai
    b += kitai
    c += kitai
    cnt += 1
    print('kitai', kitai, a)

print(cnt)

# if a >= 100:
#     cnt -= 1
#     a -= kitai
#     print('a', a)
#     sa = 100 - a
#     print('sa', sa)
#     print('kitai', kitai)
#     print('cnt', cnt)
#     cnt += sa/kitai

# if b >= 100:
#     cnt -= 1
#     b -= kitai
#     sa = 1 - b
#     cnt += sa/kitai

# if c >= 100:
#     cnt -= 1
#     c -= kitai
#     sa = 1 - c
#     cnt += sa/kitai

# print(cnt)
