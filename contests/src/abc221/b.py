import copy

S = list(input())
T = list(input())


def eq_list(l1, l2):
    for i in range(len(l1)):
        if(l1[i] != l2[i]):
            return False
    return True


l = len(T)
idx = 0

if eq_list(S, T):
    print('Yes')
    exit(0)


while idx+1 < l:
    temp = copy.copy(T)
    a = temp[idx]
    temp[idx] = temp[idx + 1]
    temp[idx + 1] = a

    # print(S, temp)
    if eq_list(S, temp):
        print('Yes')
        exit(0)
    idx += 1

print('No')
