try:
    age = input("Enter your age: ")

    
    age = int(age)

    if age < 0:
        print("Age cannot be negative.")
    else:
        if age % 2 == 0:
            print("The age is an even number.")
        else:
            print("The age is an odd number.")

except ValueError:
    print("Invalid input! Please enter a valid integer age.")
