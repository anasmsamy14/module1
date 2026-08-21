import numpy as np


arr = np.linspace(0, 9, 10, dtype=int)

print("Original Array:")
print(arr)



odd_replaced = arr.copy()
odd_replaced[odd_replaced % 2 == 1] = -1

print("\nOdd numbers replaced with -1:")
print(odd_replaced)



arr_2d = arr.reshape(2, 5)

print("\n2D Array:")
print(arr_2d)



even_sum = 0

for number in arr:
    if number % 2 == 0:
        even_sum += number

print("\nSum of all even numbers:")
print(even_sum)