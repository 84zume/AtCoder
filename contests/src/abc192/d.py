X = str(input())
M = int(input())


def base_n_to_10(X, n):
    ans = 0
    for i in range(1, len(str(X))+1):
        ans += int(X[-i])*(n**(i-1))
    return ans


d = int(max(X))+1
# print(d)

if len(X) == 1 and int(X) < M:
    print(0)
    exit(0)


xd = base_n_to_10(X, d)
count = 0
if xd <= M:
    count += 1
while xd < M:
    d += 1
    xd = base_n_to_10(X, d)
    # print(xd)
    if xd <= M:
        count += 1
print(count)
