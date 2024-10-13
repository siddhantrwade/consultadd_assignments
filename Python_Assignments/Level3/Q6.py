class Animal:

    def __init__(self, name):

        self.name = name

    def speak(self):
        return "General Animal Sound"
    
class Mammal(Animal):
    
    def __init__(self, name, category):

        super().__init__(name)
        self.mammal_kind = category

    def mammal_display(self):
        return f"{self.name} is {self.mammal_kind} mammal"
    

class Dog(Mammal):
    
    def __init__(self, name, owner_name):
        super().__init__(name, 'domestic')
        self.owner_name = owner_name

    def speak(self):
        return "woof!"
    

dog = Dog("Tommy", "Alice")

print(f"{dog.owner_name} owns a dog named {dog.name}")
print(dog.mammal_display())
print(f"dog.name says: {dog.speak}")
