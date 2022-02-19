from stack import Stack


def logic1(A):
    s = Stack()
    for a in A:
        print(a, str(s))
        if a == '(':
            s.push('(')
        else:
            s.pop()
    return s


def logic2(A):
    s = Stack()
    for i in range(len(A)):
        if A[i] == '(':
            s.push(['(', i])
        else:
            v = s.pop()
            print(v[1], i)
    return s


def test_kakko_success2():
    A = "(()())()"
    s = logic2(A)
    assert len(s) == 1


def test_kakko_success():
    A = "(()())()"
    s = logic1(A)
    assert len(s) == 0


def test_kakko_success():
    A = "(()())(()"
    s = logic1(A)
    assert len(s) != 0
