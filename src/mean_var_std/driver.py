from util import mean_var_std

if __name__ == "__main__":
    n, m = map(int, input("Enter Dimension: ").split())

    matrix = [list(map(int, input("Enter NxM: ").split())) for _ in range(n)]

    mean, var, std = mean_var_std(n, m, matrix)

    print(mean)
    print(var)
    print(round(std, 11))
