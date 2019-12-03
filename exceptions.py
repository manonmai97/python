student = {
    "name": "mark",
    "student_id": 10,
    "feedback": "none"
}

print(student["name"])
print(student.keys())
print(student.values())
student["name"]= "alex"
print(student["name"])
student["age"] = 25
print(student["name"])
print(student["age"])
student["last_name"] = "kowaski"

try:
    last_name = student["last_name"] 
    number_last_name = 3 + last_name
except KeyError:
    print("error finding last_name") 
except Exception:
    print("unknown error")
  
print("this code executes")    


