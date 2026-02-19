from util import find_percentage

if __name__ == '__main__':
    try:
        n=int(input("Enter Count: "))
        result=find_percentage(n)
        print(f"Query result: {result:.2f}")
    except Exception as e:
        print(e)