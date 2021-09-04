S = str(input())

len_S = len(S)
start = 0
end = 3

result = 999
while end <= len_S:
    # print(int(S[start:end]))
    result = min(abs(int(S[start:end]) - 753), result)
    start += 1
    end += 1

print(result)
