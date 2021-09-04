def saiki(val, level, M):
    global all_count
    if level == 7:
        count = 0
        for m in M[level]:
            if val <= m:
                count += 1
        return count
    else:
        for m in M[level]:
            if val <= m:
                saiki(m, level+1, M)


S = input()
C = 'chokudai'

c = []
h = []
o = []
k = []
u = []
d = []
a = []
i_ = []

for i in range(len(S)):
    if S[i] == 'c':
        c.append(i)
    elif S[i] == 'h':
        h.append(i)
    elif S[i] == 'o':
        o.append(i)
    elif S[i] == 'k':
        k.append(i)
    elif S[i] == 'u':
        u.append(i)
    elif S[i] == 'd':
        d.append(i)
    elif S[i] == 'a':
        a.append(i)
    elif S[i] == 'i':
        i_.append(i)

m = []
m.append(c)
m.append(h)
m.append(o)
m.append(k)
m.append(u)
m.append(d)
m.append(a)
m.append(i_)

# for val_c in c:
#     for i in range(1,7):


# for i in range(7):
#     if i == 0:
#         for v in m[i]:


all_count = 0
saiki(0, 0, m)
print(all_count)
