N = int(input())
s = str(input())

s = s.replace('fffoxoxox', '')
s = s.replace('ffofoxxox', '')
s = s.replace('foffoxoxx', '')
s = s.replace('fofofoxxx', '')
s = s.replace('ffoxox', '')
s = s.replace('fofoxx', '')

while('fox' in s):
    s = s.replace('fox', '')

print(len(s))
