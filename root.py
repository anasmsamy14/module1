import math
import cmath

# Using math.sqrt() for positive numbers
number = 16
sqrt_num = math.sqrt(number)
print(f"The square root of {number} is {sqrt_num}")

# Using the exponentiation operator
number_2 = 25
sqrt_num_2 = number_2 ** 0.5
print(f"The square root of {number_2} is {sqrt_num_2}")

# Using cmath.sqrt() for negative or complex numbers
complex_num = -9
sqrt_complex_num = cmath.sqrt(complex_num)
print(f"The square root of {complex_num} is {sqrt_complex_num}")
