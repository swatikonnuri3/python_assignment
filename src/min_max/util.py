import numpy

def min_max(n,m):
    arr = numpy.array([list(map(int, input("Enter M x N: ").split())) for _ in range(n)])
    print(numpy.max(numpy.min(arr, axis=1)))