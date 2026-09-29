students = {
    "Ana" : [90, 89, 94],
    "Kirk" : [98, 74, 90],
    "Liza" : [90, 97, 83]
}
highest  = 0
namehighest = ""
lowest = float("inf")
namelowest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "\nAverage: ", average)
    if average > highest:
        highest = average
        namehighest = name
    elif average < highest:
        lowest = average
        namelowest = name
    for g in grade:
            if g < 75:
                tally = tally+1
print("\nStudent ", namehighest,  " got the highest average: ", highest)
print("Student ", namelowest, " got the lowest average: ", lowest)
print("There are ", tally, " grades which are below 75.")
