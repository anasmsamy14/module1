class Dog:
    animal = "Dog"   
    def __init__(self, name, breed):
        self.name = name     
        self.breed = breed    



dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")


print(Dog.animal, dog1.name, dog1.breed)
print(Dog.animal, dog2.name, dog2.breed)