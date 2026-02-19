from util import time_delta

if __name__ == '__main__':
    with open('output.txt', 'w') as fptr:
        t = int(input("Enter Count: "))
        for t_itr in range(t):
            t1 = input("Enter Time 1: ")
            t2 = input("Enter Time 2: ")
            delta = time_delta(t1, t2)
            fptr.write(delta + '\n')