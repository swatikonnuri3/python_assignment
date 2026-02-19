from util import mean_var_std

if __name__=="__main__":
    n, m = map(int, input("Enter Dimension: ").split())
    mean_var_std(n,m)