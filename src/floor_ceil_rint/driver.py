from util import print_fcr
import numpy

if __name__ == "__main__":
    A = numpy.array(input("Enter Array: ").split(), float)
    floor, ceil, rint = print_fcr(A)

    print(floor)
    print(ceil)
    print(rint)
