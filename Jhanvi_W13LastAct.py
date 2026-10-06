Jhanvi_employee = {
    "E100" : {
        "Name" : "Llane Uy",
        "Rank" : "JO S",
        "Duty Hours" : (42, 43, 40, 40),
        "Basicpay" : 29000,
        "Required Hours" : 160
    },
    "E105" : {
        "Name" : "Robert Santos",
        "Rank" : "Manager 1",
        "Duty Hours" : (30, 35, 31, 30),
        "Basicpay" : 60000,
        "Required Hours" : 120
   },
    "E11" : {
        "Name" : "Lee Alina",
        "Rank" : "CEO",
        "Duty Hours" : (20, 35, 40, 30),
        "Basicpay" : 70000,
        "Required Hours" : 200
    },
}
Jhanvi_search = input("Enter employee ID to search: ").title()
for Jhanvi_id, Jhanvi_details in Jhanvi_employee.items():
    if Jhanvi_id == Jhanvi_search:
        print("Employee ID: ", Jhanvi_id)
        Jhanvi_excess = 0
        Jhanvi_dutyhrs = Jhanvi_details["Duty Hours"]
        Jhanvi_totalhrs = sum(Jhanvi_dutyhrs)
        print("\nEmployee ID: ", Jhanvi_id)
        print("Name: ", Jhanvi_details["Name"])
        print("Job Rank: ", Jhanvi_details["Rank"])
        print("Duty Hours: ", *Jhanvi_dutyhrs)
        print("Basicpay: ", Jhanvi_details["Basicpay"])
        print("Required Hours: ", Jhanvi_details["Required Hours"])
        print("Total Duty Hours: ", Jhanvi_totalhrs)

        if Jhanvi_totalhrs > Jhanvi_details["Required Hours"]:
            Jhanvi_excess = sum(Jhanvi_dutyhrs) - Jhanvi_details["Required Hours"]
            print("Excess Hour: ", Jhanvi_excess)
        else:
            print("Excess Hour: ", Jhanvi_excess)

        Jhanvi_rate = Jhanvi_details["Basicpay"] / Jhanvi_details["Required Hours"]
        print("Rate Per Hour: ", Jhanvi_rate)
        Jhanvi_overtime = Jhanvi_rate * 1.5 * Jhanvi_excess
        print("Overtime: ", Jhanvi_overtime)
        Jhanvi_grosspay = Jhanvi_details["Basicpay"] + Jhanvi_overtime
        print("Gross Pay: ", Jhanvi_grosspay)
        break
else:
    print("Employee ID Not Found.")




