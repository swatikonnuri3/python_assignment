from util import second_max

if __name__ == "__main__":
    n = int(input("Enter Size: "))
    arr = list(map(int, input("Enter Elements: ").split()))
    print(second_max(arr))
