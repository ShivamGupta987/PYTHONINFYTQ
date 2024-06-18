# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
    
# cal = Calculator()

# print(cal.add(5,6,7))

# explicicit not working in python

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
    
# cal = Calculator()

# print(cal.add(5,6,7))
# print(cal.add(5,6))

# implicit working

class Calculator:
   
    def add(self,a,b,c=0):
        return a+b+c
    
cal = Calculator()

print(cal.add(5,6,7))
print(cal.add(5,6))


