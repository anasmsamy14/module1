units = int(input('enter number of units used = '))
if(units < 50):
    bill= 2.6*units+25
    print(bill,'is your electricity bill')
elif(units > 50 and units <= 100):
    bill= 3.25*units+35
    print(bill,'is your electricity bill')
elif(units > 100 and units<= 200) :
    bill= 5.26*units +45
    print(bill,'is your electricity bill')
else :
    bill= 8.45*units+75
    print(bill,'is your electricity bill')  


    