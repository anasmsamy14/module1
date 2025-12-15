def m (x):
    '''this is a recursion function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x * m(x-1)




w=int(input('enter a number you the factorial of: '))
print(m.__doc__)
print ('the result is',m (w))