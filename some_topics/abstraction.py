from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    # Abstract method
    @abstractmethod
    def make_sound(self):
        pass

    # Concrete method
    def sleep(self):
        print("This animal is sleeping")

# Subclass implementing the abstract method
class Dog(Animal):

    def make_sound(self):
        print("Woof!")

# Subclass implementing the abstract method
class Cat(Animal):

    def make_sound(self):
        print("Meow!")

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the implemented abstract method
dog.make_sound()  
cat.make_sound() 

# Call the concrete method from the abstract class
dog.sleep() 
cat.sleep()  
