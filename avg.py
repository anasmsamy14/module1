o= [1,2,3,4,5,6]
print ("og list is:",o)
count = 0
for i in o:
    count +=i
avg = count/len(o)
print ("Average is:", avg)
print("Sum is:", count)
o.sort()
print("smallest number is:", o[0])
print("largest number is:", o[-1])