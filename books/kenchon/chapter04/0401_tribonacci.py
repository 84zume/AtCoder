def tribonacci(idx):
    if idx == 0 :
        return 0
    if idx == 1:
        return 0
    if idx == 2:
        return 1
    return tribonacci(idx-1) + tribonacci(idx-2) + tribonacci(idx-3)

n = int(input())
print(tribonacci(n))