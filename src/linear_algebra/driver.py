from util import lin_alg

if __name__ == "__main__":
    n = int(input("Enter N: "))
    matrix = [list(map(float, input().split())) for _ in range(n)]

    result = lin_alg(n, matrix)
    print(result)
