from collections import namedtuple

def named_tuple(n):
    Student = namedtuple('Student', input("Enter Column Details: ").split())

    total_marks = sum(int(Student(*input(f"Enter Column {i+1} Values: ").split()).MARKS) for i in range(n))
    average = total_marks / n
    print(f"Average: {average:.2f}")