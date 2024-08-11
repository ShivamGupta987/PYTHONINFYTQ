# aprewnt
class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        Animal.__init__(self,name)
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# --------------------superkeyword-------------

# 1st use case access the parent propertires

class Parent : 
    property = 90 
    
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
obj = Child()

obj.display()
        
# 2nd use case
class Parent : 
    property = 90 
    
    def eat(self):
        print('Parent is eating')
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
    def eat(self):
        print("Child eating")
        
        # same method child aur parent me horha usse bolte hai ,ethod overriding
        
    def calleat(self):
        self.eat()
        super().eat()
        
        
obj = Child()

obj.display()
obj.calleat()
        

# using super for aclling 

class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        super().__init__(name)  #call the parent constructor or initailizer 
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# Types of inheritance  
# single inheritance  

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
# multilevel inheritance

# animal is a parent of dog and dog is a parent of pet
class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
class Pet(Dog):
    def __init(self,name,type,houseName):
        super().__init__(name,type)
        self.houseName = houseName
        
        
# hierachical inheritance

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
class Cat(Animal):
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 

# multi inheritance
# parent
class A :
    def meth1(self):
        print('hy a')

# parent
        
class B:
    def meth2(self):
        print('hy B')
        
#  c both child of a and b dono ka info lega c

        
class C(A,B) :
    def meth(self):
        print('heelo from child')
        
    
c = C()

c.meth1()
c.meth2()

# To find order 
print(C.__mro__)
    
     
# Hybird inheritance

class Pet(Dog,Cat):
    pass


# mxnfds
# aprewnt
class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        Animal.__init__(self,name)
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# --------------------superkeyword-------------

# 1st use case access the parent propertires

class Parent : 
    property = 90 
    
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
obj = Child()

obj.display()
        
# 2nd use case
class Parent : 
    property = 90 
    
    def eat(self):
        print('Parent is eating')
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
    def eat(self):
        print("Child eating")
        
        # same method child aur parent me horha usse bolte hai ,ethod overriding
        
    def calleat(self):
        self.eat()
        super().eat()
        
        
obj = Child()

obj.display()
obj.calleat()
        

# using super for aclling 

class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        super().__init__(name)  #call the parent constructor or initailizer 
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# Types of inheritance  
# single inheritance  

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
# multilevel inheritance

# animal is a parent of dog and dog is a parent of pet
class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
class Pet(Dog):
    def __init(self,name,type,houseName):
        super().__init__(name,type)
        self.houseName = houseName
        
        
# hierachical inheritance

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
class Cat(Animal):
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 

# multi inheritance
# parent
class A :
    def meth1(self):
        print('hy a')

# parent
        
class B:
    def meth2(self):
        print('hy B')
        
#  c both child of a and b dono ka info lega c

        
class C(A,B) :
    def meth(self):
        print('heelo from child')
        
    
c = C()

c.meth1()
c.meth2()

# To find order 
print(C.__mro__)
    
     
# Hybird inheritance

class Pet(Dog,Cat):
    pass

# jsnfkj
# aprewnt
class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        Animal.__init__(self,name)
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# --------------------superkeyword-------------

# 1st use case access the parent propertires

class Parent : 
    property = 90 
    
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
obj = Child()

obj.display()
        
# 2nd use case
class Parent : 
    property = 90 
    
    def eat(self):
        print('Parent is eating')
class Child(Parent):
    property = 99 
    
    def display(self):
        print('child property: ',self.property)
        print('child property: ',super().property)
        
    def eat(self):
        print("Child eating")
        
        # same method child aur parent me horha usse bolte hai ,ethod overriding
        
    def calleat(self):
        self.eat()
        super().eat()
        
        
obj = Child()

obj.display()
obj.calleat()
        

# using super for aclling 

class Animal :
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(self.name + " animal is eating")
        
        # child
class Dog(Animal):
    def __init__(self,name,type):
        #call the conmstructor or initializer of animal'
        super().__init__(name)  #call the parent constructor or initailizer 
        self.type = type
        
    def getTheNameofDogs(self):
        print(self.name)
        
 # inheritance all th public properties both are inherited
dog = Dog('Moti','Dobberman')
dog.getTheNameofDogs()
dog.eat()


# Types of inheritance  
# single inheritance  

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
# multilevel inheritance

# animal is a parent of dog and dog is a parent of pet
class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
        
class Pet(Dog):
    def __init(self,name,type,houseName):
        super().__init__(name,type)
        self.houseName = houseName
        
        
# hierachical inheritance

class Animal : 
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print('animal is eating')
        
class Dog(Animal):
    
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 
        
class Cat(Animal):
    def __init(self,name,type):
        super().__init__(name)
        self.type = type 

# multi inheritance
# parent
class A :
    def meth1(self):
        print('hy a')

# parent
        
class B:
    def meth2(self):
        print('hy B')
        
#  c both child of a and b dono ka info lega c

        
class C(A,B) :
    def meth(self):
        print('heelo from child')
        
    
c = C()

c.meth1()
c.meth2()

# To find order 
print(C.__mro__)
    
     
# Hybird inheritance

class Pet(Dog,Cat):
    pass