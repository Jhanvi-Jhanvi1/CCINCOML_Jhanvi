#SET A
while True:
    Jhanvi_name = input("Enter Employee Name: ").title()
    Jhanvi_job = input("Enter Job Position(Janitor, Clerk, Cashier, Manager): ").title()
    Jhanvi_hours = int(input("Enter Actual Hours Worked: "))
    Jhanvi_deduct = 0
    Jhanvi_overpay = 0
    Jhanvi_overtime = 0
    Jhanvi_absent = 0
    Jhanvi_MS = 0
    match (Jhanvi_job):
        case "Janitor":
            Jhanvi_MS = 18000
        case "Clerk":
            Jhanvi_MS = 22000
        case "Cashier":
            Jhanvi_MS = 24000
        case "Manager":
            Jhanvi_MS = 40000
        case _:
            print("Invalid")

    Jhanvi_monthly = Jhanvi_MS / 2
    Jhanvi_hourlyrate = Jhanvi_monthly / 88

    if (Jhanvi_hours < 88):
        Jhanvi_absent = 88 - Jhanvi_hours
        Jhanvi_deduct = Jhanvi_absent * Jhanvi_hourlyrate
    else:
        Jhanvi_overtime = Jhanvi_hours - 88
        Jhanvi_overrate = Jhanvi_hourlyrate * 1.25
        Jhanvi_overpay = Jhanvi_overtime * Jhanvi_overrate

    Jhanvi_netsalary = Jhanvi_monthly - Jhanvi_deduct + Jhanvi_overpay
    if Jhanvi_MS != 0 and Jhanvi_hours != 0:
        print("\n-----EMPLOYEE DETAIL-----")
        print(f"Employee Name: {Jhanvi_name}")
        print(f"Job Position: {Jhanvi_job}")
        print(f"Actual Hours Worked: {Jhanvi_hours}")
        print(f"Monthly Salary: {Jhanvi_MS}")
        print(f"Basic/Gross Half-Month Salary: {Jhanvi_monthly}")
        print(f"Hourly Rate: {Jhanvi_hourlyrate:,.2f}")
        print(f'Absent Hours: {Jhanvi_absent}')
        print(f"Absent Deduction: {Jhanvi_deduct:,.2f}")
        print(f"Overtime Hours: {Jhanvi_overtime}")
        print(f"Overtime Pay: {Jhanvi_overpay:,.2f}")
        print(f"Net Half-Month Salary: {Jhanvi_netsalary:,.2f}")
    else:
        print("Cannot be processed.")
        continue

    Jhanvi_again = input("Do you want to enter again? Enter (Y/N): ").upper()
    if Jhanvi_again == "N":
        print("Program Ended")
        break



