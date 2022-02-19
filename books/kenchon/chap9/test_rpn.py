from stack import Stack


def test_rpn():
    A = [3, 4, '+', 1, 2, '-', '*', r'/']
    s = Stack()
    for a in A:
        if a == '+':
            a1 = s.pop()
            a2 = s.pop()
            a3 = a2 + a1
            s.push(a3)
        elif a == '-':
            a1 = s.pop()
            a2 = s.pop()
            a3 = a2 - a1
            s.push(a3)
        elif a == '*':
            a1 = s.pop()
            a2 = s.pop()
            a3 = a2 * a1
            s.push(a3)
        elif a == r'/':
            a1 = s.pop()
            a2 = s.pop()
            a3 = a2 / a1
            s.push(a3)
        else:
            s.push(a)
    assert str(s) == '[-7]'
