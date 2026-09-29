while True:
    Jhanvi_number = input("Enter a list of numbers with spaces: ").split()
    Jhanvi_number = [int(num) for num in Jhanvi_number]
    print(f"Your List: {Jhanvi_number}")
    Jhanvi_search = int(input("Enter a number to search for: "))

    Jhanvi_found = False

    for Jhanvi_num in Jhanvi_number:
        if Jhanvi_num == Jhanvi_search:
            Jhanvi_found = True
            break
    if Jhanvi_found:
        print(f"Number Found, It is {Jhanvi_search}")
    else:
        print("Number not found.")

    Jhanvi_again = input("Try Again? Enter (Y/N): ").strip().upper()
    if Jhanvi_again == "N":
        print("Program Ended.")
        break