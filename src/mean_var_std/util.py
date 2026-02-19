import numpy
def mean_var_std(n,m):
    arr = numpy.array([list(map(int, input("Enter NxM: ").split())) for _ in range(n)])
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(round(numpy.std(arr), 11))