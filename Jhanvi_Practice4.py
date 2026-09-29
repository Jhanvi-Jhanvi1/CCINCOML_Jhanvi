Jhanvi_students = {}

Jhanvi_num = int(input("Enter number of students: "))

for i in range(Jhanvi_num):
    print("\nStudent", i+1)

    name = input("Enter student name: ")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    Jhanvi_students[name] = (grade1, grade2, grade3)

print("---Student Access---")
for name, grades in Jhanvi_students.items():
    average = sum(grades)/len(grades)

    print(name, *grades, "Average: ", round(average))
highest = 0
nameHighest = ("")
tally = 0

for name, grade in Jhanvi_students.items():
    average = sum(grade)/len(grade)
    if average>highest:
        highest = average
        nameHighest = name
    for g in grade:
        if g < 75:
            tally = tally+1
print(f"\nStudent {nameHighest} got the highest average: {highest}")
print(f"There are {tally} grades which are below 75.")