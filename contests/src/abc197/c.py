import itertools

N = int(input())
A = list(map(int, input().split()))

patterns = list(itertools.product(range(2), repeat=N-1))

final_result = 10000000000000000

for p in patterns:
    or_result = []
    result = 0
    print(p)
    for i in range(N):
        print('#', i, p[i-1], A[i])
        if p[i-1] == 1:
            or_result.append(result)
            result = 0
        else:
            result |= A[i]
    or_result.append(result)

    for o in or_result:
        print('or_r', o)

    result2 = or_result[0]
    for i in range(1, len(or_result)):
        result2 ^= or_result[i]
    final_result = min(final_result, result2)

print(final_result)
