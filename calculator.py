a=int(input('enter a number: ' ))
i= int(input('enter a number: ' ))
def add (p,q):   
    sum1=p+q
    return sum1
def sub (p,q):
    if p>q:
        sum2=p-q
    else:
        sum2=q-p
    return sum2
def divide(p,q):
    sum3=p/q 
    return sum3
def multiply(p,q):
    sum4=p*q 
    return sum4
print (add (a,i))
print (sub (a,i))
print(divide (a,i))
print (multiply (a,i))


