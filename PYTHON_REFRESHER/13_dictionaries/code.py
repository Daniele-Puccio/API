friends=[
    {"name": "Bob", "age": 20},
    {"name":"Adam", "age": 30},
    {"name":"Anne", "age": 27}
]
print(friends[0]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}:{attendance}")

if "Bob" in student_attendance:
    print(f"Bob student: {student_attendance['Bob']}")
else:
    ("Bob isn't a student!")

attendance_value=student_attendance.values()
print(sum(attendance_value)/len(attendance_value))