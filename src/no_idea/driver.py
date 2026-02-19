from util import calculate_happiness

if __name__ == "__main__":
    n, m = map(int, input("Enter Array Size & Set Size: ").split())
    arr = list(map(int, input("Enter Array Elements: ").split()))
    set_a = set(map(int, input("Enter Liked Elements: ").split()))
    set_b = set(map(int, input("Enter Disliked Elements: ").split()))
    print("Your Happiness Score is: ",calculate_happiness(arr, set_a, set_b))