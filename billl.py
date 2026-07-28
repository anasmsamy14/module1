def calculate_change(total_bill, amount_paid):
    change = amount_paid - total_bill
    return change



bill = 2.50
paid = 4.00

returned_money = calculate_change(bill, paid)

print("The shopkeeper should return:", returned_money, "dollars")
