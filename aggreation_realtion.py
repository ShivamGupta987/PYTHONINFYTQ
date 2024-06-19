
# HAS-A :- Aggreagation relation
class Car : 
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color 
        
class Person : 
    def __init__(self,name,car):
        self.name = name
        self.car = car 
        
        # b me se car aggregate ho rha that is known as gagreation relationship
        
car = Car('BMW','WHITE')
b= Person('Shivam',car)