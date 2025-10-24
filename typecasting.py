name="anas"
print("name =", name, type(name))
age=12
print("age =",age, type(age))
student=True
print("student =",student,type(student))
wight=32.25
print("wight =",wight,type(wight))

print("AFTER TYPECASTING...")

name=bool(name)
print(type(name))
age=str(age)
print(type(age))
student=float(student)
print(type(student))
wight=int(wight)
print(wight,type(wight))


