Jhanvi_classrecord = {
    "Liza" : {
        "StudID" : "5001",
        "Grade" : [90, 85, 86, 82, 83, 91, 92]
    },
    "Jeremy" : {
        "StudID" : "5002",
        "Grade" : [72, 75, 69, 80, 84, 75, 85]
    },
    "Jasmin" : {
        "StudID" : "5003",
        "Grade" : [72, 59, 69, 71, 51, 65, 64]
    },
    "Johnny" : {
        "StudID" : "5004",
        "Grade" : [59, 60, 89, 90, 91, 92, 95]
    },
    "Alina" : {
        "StudID" : "5005",
        "Grade" : [79, 60, 86, 90, 93, 92, 94]
    }
}
#TO SEARCH NAME OF STUDENT
Jhanvi_search = input("Enter name of student to search for: ").title()
for Jhanvi_name, Jhanvi_details in Jhanvi_classrecord.items():
    if Jhanvi_name == Jhanvi_search:
        print("\nName Found: ", Jhanvi_name)

        #TO DISPLAY GRADE, IF NAME IS FOUND
        Jhanvi_grades = Jhanvi_details["Grade"]
        print("Grades: ", *Jhanvi_grades)

        #DISPLAY AVERAGE, HIGHEST, LOWEST, AND CHECK IF NEED FOR INTERVENTION
        Jhanvi_average = sum(Jhanvi_grades) / len(Jhanvi_grades)
        print(f"Average: {Jhanvi_average:.2f}")
        print("Highest Grade: ", max(Jhanvi_grades))
        print("Lowest Grade: ", min(Jhanvi_grades))
        if min(Jhanvi_grades) < 60:
            print("Candidate for intervention")
        break
#IF NAME NOT IN LIST, DISPLAY "NOT FOUND"
else:
    print("Not Found.")
