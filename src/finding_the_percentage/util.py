def find_percentage(n):
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter details: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter query name: ")
    if query_name not in student_marks:
        raise ValueError(f"No records found for {query_name}")

    return sum(student_marks[query_name]) / len(student_marks[query_name])