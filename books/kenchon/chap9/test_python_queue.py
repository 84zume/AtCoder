"""
pythonのQueueの実装は2つある。
collections.deque→高速、ただしシングルスレッド
queue.Queue→スレッドセーフ
"""

from collections import deque
import queue


def test_deque():
    d = deque()
    d.append(1)
    d.append(2)
    d.append(3)
    a1 = d.popleft()
    assert a1 == 1


def test_Queue():
    d = queue.Queue()
    d.put(1)
    d.put(2)
    d.put(3)
    a1 = d.get()
    assert a1 == 1
