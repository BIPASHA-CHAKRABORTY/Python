class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return super().sound() + " but specifically barking!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)       
print(dog.breed)
print(dog.sound())    
