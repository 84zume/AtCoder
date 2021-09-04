N, A, B = map(int, input().split())

souwa = 0

for n in range(1, N+1):
    str_n = str(n)
    keta_wa = 0
    for e in str_n:
        keta_wa += int(e)
    # print("n:", n, "keta_wa:", keta_wa)
    if A <= keta_wa and keta_wa <= B:
        souwa += n

print(souwa)
