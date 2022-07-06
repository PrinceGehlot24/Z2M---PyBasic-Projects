
student_scores = {
    "Ram": 56,
    "Shyam": 96,
    "Raman": 71,
    "Rohan": 43,
    "Kirti": 26,
    "John": 36,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 70:
        student_grades[student] = "Exceeds Expectation"
    elif score > 40:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
