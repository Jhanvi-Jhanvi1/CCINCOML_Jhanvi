students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95
}
print("Student Grades")

print("Ana:", students["Ana"])
print("Ben:", students["Ben"])

students["Ellen"] = 92

students["Carlo"] = 82
students["Diana"] = 91

name1 = input("Enter student name: ").title()
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)

for name, grade in students.items():
    print(name, "", grade)

search = input("Enter name of student to search: ").title()
if search in students:
    print(search, "has a grade of", students[search])
else:
    print("Student name not found")