num1= [1,23,4,5]
num2= [3,4,5,8,4]
result = map(lambda x, y: x+y ,num1,num2)
print('add of two  list', list (result))
nums= [1,2,3,4,90]
def sq (n):
    return n*n
square= list(map(sq,nums))
print ("square of nums in list is ",square)
    