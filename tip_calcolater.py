def mu (bill_amount, tip_perc):
    total = bill_amount * (1+ 0.01 * tip_perc)
    total= round(total,2)
    print(f'please pay l.e{total}')
amount= float(input("enter bill amount"))
tip = int(input("enter tip perentage"))
mu (amount,tip)    