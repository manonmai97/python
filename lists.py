student_names = ["mark", "jessy", "alex"]
print(student_names)
print(student_names[1])
print(student_names[-1])
student_names[0] = "james"
print(student_names)
student_names.append("bart")
print(student_names)

print("mark" in student_names)
print(len(student_names))

student_names.append("elle")
print(student_names)
print(len(student_names))
student_names[0] = "none"
print(student_names)
print(len(student_names))
del(student_names[0])
print(student_names)
print(student_names[1:-1])