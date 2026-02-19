from util import find_word_order

if __name__ == "__main__":
    n = int(input("Enter No.of Words: "))
    words = [input(f"Enter Word {i+1}: ").strip() for i in range(n)]
    dct = find_word_order(n, words)
    print(f"Distinct Words: {len(dct)}")
    print(f"Their Occurrences: {" ".join(map(str, dct.values()))}")