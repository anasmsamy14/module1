
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)


def calculate_product(tup):
    result = 1
    for number in tup:
        result *= number
    return result


print(f"Product of tup1: {calculate_product(tup1)}")
print(f"Product of tup2: {calculate_product(tup2)}")
