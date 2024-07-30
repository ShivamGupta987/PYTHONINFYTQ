
# stack with the help of linked list
class Stack:
    # constructor
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
    
    def printresult(self):
        return self.stack
        
s = Stack()
s.push(3)
s.push(4)
s.push(5)

s.push(6)
print(s.printresult())

s.pop()
s.pop()

print(s.printresult())


class Stack:
    # constructor
    def __init__(self) -> None:
        self.stack = []
    # print reverse
    def push(self,value):
        self.stack = [value]+self.stack
    def pop(self):
        self.stack.pop()
    
    def printresult(self):
        return self.stack
        
s = Stack()
s.push(3)
s.push(4)
s.push(5)

s.push(6)
print(s.printresult())

s.pop()
s.pop()

print(s.printresult())


# stack with the linked list 

class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None 
        
class Stack:
    def __init__(self) -> None:
        self.head = None 
        
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.head is None:
            raise IndexError("stack is empty")
        popped_value = self.head.data 
        self.head = self.head.next 
        return popped_value 
    def print(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(3)

    s.push(3)
    s.print()

    
    
        