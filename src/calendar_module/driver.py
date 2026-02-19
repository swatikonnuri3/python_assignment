from util import get_day

if __name__=="__main__":
    m, d, y = map(int, (input("Enter M-D-Y: ").split()))
    get_day(m,d,y)