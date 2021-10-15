import numpy as np


def getNearestIndex(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return idx


l1 = [1, 2, 3, 4, 5]
print(getNearestIndex(l1, 3))
print(getNearestIndex(l1, 1))
print(getNearestIndex(l1, 0))

l2 = [1]
print(getNearestIndex(l2, 3))
print(getNearestIndex(l2, 1))
print(getNearestIndex(l2, 0))
