

print("Welcome to Rohit's Number System Project!")
print("This program converts a decimal number into binary.\n")
decimal = int(input("Enter a decimal number: "))
binary = ""
num = decimal
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num //= 2
print(f"The binary form of {decimal} is: {binary}")
