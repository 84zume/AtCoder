x1, y1, x2, y2 = map(int, input().split())

len_x = x2 - x1
len_y = y2 - y1


if len_x >= 0 and len_y >= 0:
    print(x2-abs(len_y), y2+abs(len_x), x1-abs(len_y), y1+abs(len_x))
elif len_x < 0 and len_y >= 0:
    print(x2-abs(len_y), y2-abs(len_x), x1-abs(len_y), y1-abs(len_x))
elif len_x < 0 and len_y < 0:
    print(x2+abs(len_y), y2-abs(len_x), x1+abs(len_y), y1-abs(len_x))
elif len_x >= 0 and len_y < 0:
    print(x2+abs(len_y), y2+abs(len_x), x1+abs(len_y), y1+abs(len_x))


# if(x1 != x2):
#     len = abs(x1-x2)
# else:
#     len = abs(y1-y2)

# if x1 < x2 and y1 == y2:
#     print(x2, y2+len, x1,  y2+len)
# elif x1 == x2 and y1 < y2:
#     print(x1-len,  y2, x1-len, y1)
# elif x2 < x1 and y1 == y2:
#     print(x2, y2-len, x1,  y2-len)
# elif y1 > y2 and x1 == x2:
#     print(x1+len, y2, x1+len, y1)
