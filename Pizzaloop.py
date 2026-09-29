# Jhanvi_flavor = [("Pepperoni", "Small", 200), ("Pepperoni", "Medium", 400), ("Pepperoni", "Large", 800),
#                 ("Truffle", "Small", 300), ("Truffle", "Medium", 500), ("Truffle", "Large", 900)]

Jhanvi_flavor = ["Pepperoni", "Truffle Mushroom"]
Jhanvi_choice = input("Enter the pizza flavor (Pepperoni/Truffle): ").lower()
match Jhanvi_flavor:
    case "pepperoni":
        print("You chose Pepperoni Pizza.")

        Jhanvi_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
        if Jhanvi_size == "small":
            Jhanvi_price = 200
        elif Jhanvi_size == "medium":
            Jhanvi_price = 400
        elif Jhanvi_size == "large":
            Jhanvi_price = 800
        else:
            Jhanvi_price = 0
            print("Invalid size.")

    case "truffle":
        print("You chose Truffle Pizza.")

        Jhanvi_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
        if Jhanvi_size == "small":
            Jhanvi_price = 200
        elif Jhanvi_size == "medium":
            Jhanvi_price = 400
        elif Jhanvi_size == "large":
            Jhanvi_price = 800
        else:
            Jhanvi_price = 0
            print("Invalid size.")
# if Jhanvi_choice == 1:
#     Jhanvi_flavor = Jhanvi_pizza[0]
# elif Jhanvi_choice == 2:
#     Jhanvi_flavor = Jhanvi_pizza[1]
# else:
#     print("Invalid Pizza Flavor")

# print("--------PIZZA ORDERING SYSTEM-------")
# Jhanvi_price = 0
#
# match Jhanvi_flavor:
#     case "pepperoni":
#         print("You chose Pepperoni Pizza.")
#
#         Jhanvi_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
#         if Jhanvi_size == "small":
#             tajolosa_price = 200
#         elif tajolosa_size == "medium":
#             tajolosa_price = 400
#         elif tajolosa_size == "large":
#             tajolosa_price = 800
#         else:
#             tajolosa_price = 0
#             print("Invalid size.")
#
#     case "cheese":
#         print("You chose Cheese Pizza.")
#
#         tajolosa_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
#         if tajolosa_size == "small":
#             tajolosa_price = 200
#         elif tajolosa_size == "medium":
#             tajolosa_price = 400
#         elif tajolosa_size == "large":
#             tajolosa_price = 800
#         else:
#             tajolosa_price = 0
#             print("Invalid size.")
#
#     case "veggie":
#         print("You chose Veggie Pizza.")
#
#         tajolosa_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
#
#         if tajolosa_size == "small":
#             tajolosa_price = 300
#         elif tajolosa_size == "medium":
#             tajolosa_price = 500
#         elif tajolosa_size == "large":
#             tajolosa_price = 900
#         else:
#             tajolosa_price = 0
#             print("Invalid size.")
#
#     case "margherita":
#         print("You chose Margherita Pizza.")
#
#         tajolosa_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
#
#         if tajolosa_size == "small":
#             tajolosa_price = 300
#         elif tajolosa_size == "medium":
#             tajolosa_price = 500
#         elif tajolosa_size == "large":
#             tajolosa_price = 900
#         else:
#             tajolosa_price = 0
#             print("Invalid size.")
#
#     case "meat lovers":
#         print("You chose Meat Lovers Pizza.")
#
#         tajolosa_size = input("Enter the size of your Pizza (small/medium/large): ").lower()
#
#         if tajolosa_size == "small":
#             tajolosa_price = 300
#         elif tajolosa_size == "medium":
#             tajolosa_price = 500
#         elif tajolosa_size == "large":
#             tajolosa_price = 900
#         else:
#             tajolosa_price = 0
#             print("Invalid size. Please pick from the choices.")
#
#     case _:
#         tajolosa_price = 0
#         print("->", tajolosa_flavor, "is not a valid pizza flavor, please choose from the choices above.")
#
# if tajolosa_price > 0:
#     print("Your cost: P", tajolosa_price, "\n\n----CHECKOUT----")
#     tajolosa_cash = float(input("Enter the your cash amount: "))
#
#     if tajolosa_cash >= tajolosa_price:
#         tajolosa_result = tajolosa_cash - tajolosa_price
#
#         if tajolosa_result>0:
#             print("Your change is: ", tajolosa_result, "\nCUSTOMER NAME:", tajolosa_customer, "\nORDER:", tajolosa_flavor, "\nThank you for ordering!")
#         else:
#             print("CUSTOMER NAME:", tajolosa_customer, "\nORDER:", tajolosa_flavor, "\nNo change.\nThank you for ordering!")
#
#     else:
#         print("Insufficient Cash.")