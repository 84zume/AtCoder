# S = str(input())
# before = len(S)
# while ('01' in S) or ('10' in S):
#     if '01' in S:
#         S = S.replace('01', '')
#     if '10' in S:
#         S = S.replace('10', '')
# print(before - len(S))
S = str(input())

cnt0 = S.count('0')
cnt1 = S.count('1')

print(2*min(cnt0, cnt1))
