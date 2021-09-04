N = str(input())

ichi = int(N[-1])

if ichi == 2 or ichi == 4 or ichi == 5 or ichi == 7 or ichi==9:
    print('hon')
elif ichi == 0 or ichi == 1 or ichi == 6 or ichi==8:
    print('pon')
else:
    print('bon')

