from abc import ABC, abstractmethod
class abs(ABC):
    
    def print(self, x):
        print("passed value is ", x)
   
    def task(self):
        print("we are in side abstract class")   

class test(abs):
    def task(self):
        print("we are in side test class")

test_obj = test()
test_obj.task()
test_obj.print(100)

       