def test_queue_list():
    q = []
    q.append(1)
    q.append(2)
    q.append(3)
    v = q.pop(0)
    assert v == 1
