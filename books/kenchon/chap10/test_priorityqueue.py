import heapq

def test_heapq():
    a = [1,6,8,0,-1]
    heapq.heapify(a)
    v = heapq.heappop(a)
    assert v == -1

