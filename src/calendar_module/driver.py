from util import get_day

if __name__ == "__main__":
    day, month, year = map(int, input("Enter D-M-Y: ").split())
    print(get_day(day, month, year))
