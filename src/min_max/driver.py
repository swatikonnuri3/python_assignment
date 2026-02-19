from util import min_max

if __name__ == "__main__":
    n, m = map(int, input("Enter Dimension: ").split())
    matrix = [list(map(int, input("Enter M x N: ").split())) for _ in range(n)]

    result = min_max(n, m, matrix)
    print(result)
