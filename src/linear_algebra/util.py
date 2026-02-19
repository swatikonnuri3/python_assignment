import numpy

def lin_alg(n, matrix):
    arr = numpy.array(matrix, float)
    det = numpy.linalg.det(arr)
    return round(det, 2)
