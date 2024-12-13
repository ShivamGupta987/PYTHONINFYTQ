
# class Animal : 
#     def eat(self):
#         print("ani Eating...")

# class Dog(Animal):
#     def eat(self):
#         print("eating....")
# class cat(Animal):
#     def eat(self):
#         print('eating')
        
# c= cat()
# b = Dog()
# a= Animal()

# c.eat()
# b.eat()
# a.eat()

# bird flying concept using polymorphisme

class BirdFly:
    def flybird(self,bird):
        bird.fly()
        
        
class Parrot:
    def fly(self):
        print("Parrot is flying...") 
        
class Pigeon:
    def fly(self):
        print("Pigeon is flying...")
        
        
a = Parrot()
b = Pigeon()


bf = BirdFly()

bf.flybird(a)
bf.flybird(b)


        