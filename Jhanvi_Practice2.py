#DICTIONARY AND LIST
students = {
    "Ana:" : [90, 85, 82],
    "Kirk:" : [72, 73, 78]
}
for name, grade in students.items():
    print(name, *grade)

# #DICTIONARY AND TUPLE
students = {
    "Ana:" : (90, 85, 82),
    "Kirk:" : (72, 73, 78)
}
for name, grade in students.items():
    print(name, *grade)