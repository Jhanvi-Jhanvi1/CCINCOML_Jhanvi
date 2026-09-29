# i = 1
# while i<=5:
#     print(i)
#     i+=1

# for i in range(1,6):
#     print(i)

#i = controlling variable

# word = "NAMASTE"
# for character in word:
#     print(character)
#READING CHAR IN STRING

# total  = 0
# i = 1
# while(i<=10):
#     total+=1
#     i+=1
# print(f"The Sum is: {total}")
while True:
    word = input("Enter a word: ").lower()
    letter = input("Enter a character to search for: ").lower()

    found = False
    for character in word:
        if character == letter:
            found = True
            break
    if found:
        print(f"Character Found, It is {character}")
    else:
        print("Character not found.")

    again = input("Try Again? Enter (y/n): ").upper()
    if again == "N":
        break






