def find_percentage(student_marks, query_name):
    if query_name not in student_marks:
        raise ValueError("Student not found")
    scores = student_marks[query_name]
    return sum(scores) / len(scores)
