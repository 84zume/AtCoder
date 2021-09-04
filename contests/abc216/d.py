import collections


def pop_balls(a, n):
    for i in range(len(a)):
        if len(a[i]) == 0:
            continue
        if a[i][-1] == n:
            # print(i, '筒の', a[i][-1], 'を削除')
            a[i].pop()


def del_tutu(a):
    for i in reversed(range(len(a))):
        if len(a[i]) == 0:
            del(a[i])


# デバッグ用の関数


def print_tutu(a):
    print("現在の筒を表示")
    for i in range(len(a)):
        print(i, '番目の筒======')
        print(a[i])
        print('==============')
        print('')


N, M = map(int, input().split())
k = []
a = []

for i in range(M):
    input_k = int(input())
    k.append(input_k)
    input_a = list(map(int, input().split()))
    a.append(input_a)

checkcontinue = True
while checkcontinue:

    checkcontinue = False

    # デバッグ
    # print_tutu(a)

    # 筒の上のボールをすべて取り出す
    up_balls = []
    for i in range(len(a)):
        up_balls.append(a[i][-1])
    # ボールの出現回数をカウントする
    c = collections.Counter(up_balls)

    # 複数出現するボールを削除する
    for c in c.items():
        if c[1] == 2:
            pop_balls(a, int(c[0]))
            checkcontinue = True

    # 空の筒を捨てる
    del_tutu(a)
    if len(a) == 0:
        print('Yes')
        exit()

print('No')
