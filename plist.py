num = int(input("Enter number: "))

odd_numbers = [
    x
    for x in range(num)
    if x % 2 != 0
]

fruits = ["apple", "banana", "mango"]

capital_fruits =[f
    for f in fruits]

print(odd_numbers)
print(capital_fruits)