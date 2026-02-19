import numpy as np

def mean_var_std(n, m, matrix):
    arr = np.array(matrix)

    mean = np.mean(arr, axis=1)
    var = np.var(arr, axis=0)
    std = np.std(arr)

    return mean, var, std
