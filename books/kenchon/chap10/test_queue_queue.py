import queue


def test_queue_Queue():
    q = queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    v = q.get()
    assert v == 1
