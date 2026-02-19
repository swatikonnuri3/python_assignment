from util import find_percentage

if __name__ == "__main__":
    n = int(input("Enter Count: "))
    student_marks = {}

    for _ in range(n):
        name, *line = input("Enter details: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter query name: ")
    result = find_percentage(student_marks, query_name)

    if result is None:
        print("Student not found")
    else:
        print(f"Query result: {result:.2f}")
