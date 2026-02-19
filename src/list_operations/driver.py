from util import list_operations

if __name__ == '__main__':
    num = int(input())
    my_list = []

    for _ in range(num):
        command = input().split()
        operation = command[0]
        args = list(map(int, command[1:]))

        my_list = list_operations(my_list, operation, *args)

    print("Final list:", my_list)
