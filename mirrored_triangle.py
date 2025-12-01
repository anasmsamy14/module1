

print("Welcome to Radhika's Pattern Program!")
print("This program draws a mirrored right-angled triangle.")


rows = int(input("Enter the number of rows: "))

print("Mirrored Right-Angled Triangle:")


for i in range(1, rows + 1):
    
    print(" " * (rows - i), end="")
    
    print("*" * i)
