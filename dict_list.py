School = [
    {
        "name": "Abhishek",
        "RollNo": 257,
        "subjects": ["English", "Hindi", "Commerce"]
    },
    {
        "name": "Sohan",
        "RollNo": 207,
        "subjects": ["Maths", "Hindi", "Science"]
    },
]


def add_new_student(student_name, student_roll, student_sub):

    new_student = {}
    new_student["name"] = student_name
    new_student["RollNo"] = student_roll
    new_student["subjects"] = student_sub
    School.append(new_student)


add_new_student("John", 235, ["Computer", "Science", "Arts"])
print(School)
