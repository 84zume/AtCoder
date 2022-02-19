from stack import Stack


def test_stack():
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(7)
    val = s.pop()
    assert val == 7
    assert str(s) == '[5, 3]'
    s.pop()
    s.pop()
    assert len(s) == 0
