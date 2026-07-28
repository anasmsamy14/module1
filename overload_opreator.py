class A:
    def __init__(self,a):
        self.a = a
    
    def __lt__(self,other):
        if(self.a<other.a):
            return "obj1 is less than obj2"
        else:
            return "obj1 is not less than obj2"
        
    def __eq__(self, other):
        
        if(self.a==other.a):
            return 'both are equal'
        else:
            return 'both are not equal'

obj1 = A(10)
obj2 = A(20)   
print('passed values :',obj1.a, obj2.a)
print(obj1<obj2)
obj3 = A(10)
obj4 = A(10)
print('passed values :',obj3.a, obj4.a)
print(obj3==obj4)