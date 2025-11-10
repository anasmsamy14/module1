
m= str(input("do you have a medical conditions= "))
if(m=='yes'):
    print('you can take the quiz')
else:
 
    p= int(input("enter your attendance= "))
    if(p>70):
        print("you can take the test")
    else:
        print("you cant take the quiz")
        