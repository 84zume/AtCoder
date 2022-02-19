from collections import deque


def test_queue_deque():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    v = q.popleft()
    assert v == 1
