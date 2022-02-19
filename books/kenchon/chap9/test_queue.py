from queue import Queue


def test_queue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    val = q.dequeue()
    assert val == 3
    assert str(q) == '[7, 5]'
    q.dequeue()
    q.dequeue()
    assert len(q) == 0
