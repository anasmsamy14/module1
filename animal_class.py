from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can crawl")   

class lion(animal):
    def move(self):
        print("I can walk and run and roar")
class monkey(animal):
    def move(self):
        print("I can climb trees")                    
d=dog()
d.move()
s=snake()
s.move()   
l=lion()
l.move()
m=monkey()  
m.move()
