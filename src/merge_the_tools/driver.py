from util import merge_the_tools

if __name__ == "__main__":
    string = input("Enter String: ")
    k = int(input("Enter Parts Length: "))

    result = merge_the_tools(string, k)
    for item in result:
        print(item)
