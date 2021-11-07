A = list(map(int, input().split()))
sort_A = sorted(A)

ans = []
for a in A:
    ans.append(str((sort_A.index(a))))

print(' '.join(ans))
