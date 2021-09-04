H, W = map(int, input().split())
a = [str(input()) for i in range(H)]

bar = ['#']*(W+2)
print(''.join(bar))
for e in a:
    bar2 = '#' + ''.join(e) + '#'
    print(bar2)
print(''.join(bar))
