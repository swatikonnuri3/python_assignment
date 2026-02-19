def list_operations(my_list, operation, *args):
    if operation == "insert":
        index, value = args
        my_list.insert(index, value)

    elif operation == "append":
        value = args[0]
        my_list.append(value)

    elif operation == "remove":
        value = args[0]
        my_list.remove(value)

    elif operation == "sort":
        my_list.sort()

    elif operation == "pop":
        my_list.pop()

    elif operation == "reverse":
        my_list.reverse()

    return my_list
