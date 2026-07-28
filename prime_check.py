num =int(input('enter an upper range: '))
num2 = int (input('enter a lower range: '))
print ('I am going to print prime numbers from ',num2 ,'and', num)
for i in range (num2 , num):
    if i > 1:
        for e in range (2,i):
            if (i % e )==0:
                break
        else:
             print (i)
                
        
            
        