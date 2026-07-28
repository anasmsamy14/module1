class Employee():


  def __init__(self):
    print("Employee created")

  def __del__(self):
    print('Destructor called')
  
def create_obj():
  print('Making object')
  obj = Employee()
  print('Function end ....')
  return obj

print('Calling create_obj()  Funvtion....')
obj=create_obj()
print('Program End...')
     