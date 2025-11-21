b = int(input("Base: "))
e = int(input("Exponent: "))

p = 1
for i in range(e):
    p = p * b

print(p)
