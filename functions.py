students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase



def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)   

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id }
    students.append(student)     


student_list = get_students_titlecase()

student_name = input("enter student name:")
student_id = input("enter student id:")
add_student_name = input("do you want to add:")
if add_student_name: True
student_name = input("enter student name:")
    

add_student(student_name, student_id)
print_students_titlecase()

