my_set= {1,2,3,4}
print(my_set)


my_set1 = {1.5,'hi',(1,2,3,4,5,6)}
print(my_set1)


my_num = {1,2,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6}
print(my_num)


my_set2 = set([1,2,3,4,7,8,9,10])
print(my_set2)


my0_set3 = {1,3,2,5,7,3,8,9,3,5,7}
print("The original set is:", my0_set3)
my0_set3.add(1761563)
print("The set after adding an element:", my0_set3)

my0_set3.pop()

print("The set after removing an element:", my0_set3)


my0_set3.update({1,2,3,4,5,6,7,8,9})
print("The set after updating with another set:", my0_set3)

my0_set3.remove(1761563)

print("The set after removing a specific element:", my0_set3)

my0_set3.clear()


print("The set after clearing all elements:", my0_set3)


