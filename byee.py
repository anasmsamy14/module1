v= False
while not v :    
    try:
        n= int(input("enter a number: "))
        while n % 2 == 0:
            print('bye')
            break
        v= True
    except ValueError:
        print("invalid input, please enter a valid number")