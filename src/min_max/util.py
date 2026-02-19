import numpy as np

def min_max(n, m, matrix):
    arr = np.array(matrix)
    return int(np.max(np.min(arr, axis=1)))
