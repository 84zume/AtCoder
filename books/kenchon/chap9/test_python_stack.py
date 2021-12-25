
"""
pythonの場合はlistでStackを実現できる
https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-stacks
"""


def test_stack():
    s = []
    s.append(1)
    s.append(2)
    s.append(3)
    a1 = s.pop()
    s.pop()
    s.pop()
    assert a1 == 3
    assert len(s) == 0
