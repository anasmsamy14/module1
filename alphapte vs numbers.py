
user_input = input("Enter something: ")
if user_input.isdigit():
    print("You entered a number")
elif user_input.isalpha():
    print("You entered a letter.")
else:
    print("You entered something else (not just a letter or number).")
