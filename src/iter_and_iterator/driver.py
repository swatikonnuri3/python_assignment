from util import probability_with_a

if __name__ == "__main__":
    print("Enter the number of elements:")
    n = int(input().strip())
    print("Enter the elements separated by spaces:")
    l = input().strip().split()
    print("Enter the size of the combination:")
    k = int(input().strip())
    result = probability_with_a(n, l, k)
    print("Probability that a combination contains 'a':", result)