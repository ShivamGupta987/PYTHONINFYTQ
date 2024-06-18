class Person:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        # private insisde class shsow krega
        self.__salary = salary 
        
        # we calls only inside class 
        
        def findAge(self):
            return self.age 
        
        def find_Salary(self):

            print(self.salary)
            
            
per = Person('shivam',35,5000)    
# if we try to print inside they dont print that
print(per.name)

# salary show error
# print(per.salary)

#  try thtsess 

print(per._Person__salary)