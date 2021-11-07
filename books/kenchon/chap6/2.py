import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

# print(A)
# print(B)
# print(C)

for b in B:
    a_index = bisect.bisect_left(A, b)
    c_index = bisect.bisect_right(C, b)
    # print(b, a_index, c_index)
    ans += a_index * (N-c_index)
print(ans)
