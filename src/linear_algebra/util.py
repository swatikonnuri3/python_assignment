import numpy
def lin_alg(n):
    arr = numpy.array([list(map(float, input("Enter N x N: ").split())) for _ in range(n)])
    det = numpy.linalg.det(arr)
    print(round(det, 2))