Q = int(input())
query = []
for i in range(Q):
    a = input().split()
    query.append(a)

bag = []

for q in query:
    if q[0] == '1':

        bag.append(int(q[1]))
    elif q[0] == '2':
        for i in range(len(bag)):
            bag[i] += int(q[1])
    elif q[0] == '3':
        min_val = min(bag)
        print(min_val)
        bag.remove(min_val)

# ディクショナリーでやれば良さそう
