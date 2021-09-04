def is_odd_list(list):
    for elem in list:
        if elem % 2 != 0:
            return False
    return True


def replace_value(list):
    newlist = []
    for elem in list:
        newlist.append(elem / 2)
    return newlist


n = int(input())
a = list(map(int, input().split()))
cnt = 0

while(True):
    if is_odd_list(a):
        a = replace_value(a)
        cnt += 1
    else:
        break
print(cnt)
