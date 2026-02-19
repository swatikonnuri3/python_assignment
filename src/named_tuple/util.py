from collections import namedtuple

def named_tuple(n, columns, data):
    Student = namedtuple("Student", columns)

    total = 0
    for row in data:
        s = Student(*row)
        total += int(s.MARKS)

    return total / n
