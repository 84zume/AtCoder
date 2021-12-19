from linked_list import LinkedList


def test_insert_first():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    assert str(l) == '[5, 3]'


def test_insert_last():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    l.insert_last(99)
    assert str(l) == '[5, 3, 99]'


def test_len():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    assert len(l) == 2


def test_remove():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    l.remove(3)
    assert str(l) == '[5]'


def test_insert():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    l.insert_first(9)
    l.insert_first(34)
    l.insert(9, 4)
    assert str(l) == '[34, 9, 4, 5, 3]'


def test_remove_first():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    l.remove_first()
    assert str(l) == '[3]'


def test_remove_last():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    l.remove_last()
    l.remove_last()
    assert str(l) == '[]'


def test_print_begin():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    assert l.begin() == 5


def test_print_end():
    l = LinkedList()
    l.insert_first(3)
    l.insert_first(5)
    assert l.end() == 3
