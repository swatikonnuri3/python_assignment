import numpy

def print_fcr(A):
    floor = numpy.floor(A)
    ceil = numpy.ceil(A)
    rint = numpy.rint(A)

    return floor, ceil, rint
