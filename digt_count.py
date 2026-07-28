num = int(input("Enter a number: "))

count = 0
n = num

while n != 0:
    n //= 10
    count += 1

print("Digits:", count)
