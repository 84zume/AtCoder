n = int(input())
list_a = list(map(int, input().split()))
alice = 0
bob = 0

list_a.sort()
while(len(list_a) != 0):
    alice += list_a.pop()
    if(len(list_a) != 0):
        bob += list_a.pop()
sa = alice-bob
print(sa)
