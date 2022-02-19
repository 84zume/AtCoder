def tribonacci(idx, m):
    if idx == 0 :
        return 0
    if idx == 1:
        return 0
    if idx == 2:
        return 1
    if m[idx] != -1:
        return m[idx]
    
    ans = tribonacci(idx-1, m) + tribonacci(idx-2, m) + tribonacci(idx-3, m)
    memo[idx] = ans
    return ans

memo = [-1]*100
n = int(input())
print(tribonacci(n, memo))
print(memo)