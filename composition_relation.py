

class Engine:
    def enginedetails(self):
        print("Engine Details:")
        
class Tyres:
    def tyresdetails(self):
        print("tyres Details:")
class Doors:
    def doorsdetails(self):
        print("Doors Details:")
        
        # car ke bina uppare wale ka kuch nhi isliye composition relation
        
class Car:
    def __init__(self):
        self.engine = Engine()
        self.tyres = Tyres()
        self.doors = Doors()

    def printdetails(self):
        self.engine.enginedetails()
        self.tyres.tyresdetails()
        
        
        self.doors.doorsdetails()
        
c = Car()

c.printdetails()
        
        