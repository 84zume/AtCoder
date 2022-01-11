import heapq


def test_heapq():
    a = [1, 6, 8, 0, -1]
    heapq.heapify(a)
    v = heapq.heappop(a)
    assert v == -1


def test_heapq_maxheap():
    A = [1, 6, 8, 0, -1]
    A = [-1 * a for a in A]
    heapq.heapify(A)
    v = -1 * heapq.heappop(A)
    assert v == 8
