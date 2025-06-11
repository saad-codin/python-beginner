# Classes 
class Animal():  
    def __init__ (self,name,age): 
        self.name = name 
        self.age = age  
    def eat(self): 
      return f"{self.name} is eating!" 
    
    def walk(self): 
        return f"{self.name} is walking!"


class Dog(Animal): 
    def __init__ (self, name,age):
        self.name= name 
        self.age = age  

    def bark(self): 
        return "WOOF"

dog = Dog("Timmy", 20) 
print(dog.bark())   



print(dog.eat())
print(dog.age)
print(dog.walk())

