
ch = input("Enter a character: ")

if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print("You entered an alphabet.")
elif ch >= '0' and ch <= '9':
    print("You entered a number.")
else:
    print("You entered a special character.")

