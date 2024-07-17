
# create a node 

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
#  create a linked_lIst 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    #  add node to linked list 
    
    def add_node(self,value):
        new_node = Node(value) 
        
        # create head node 
        
        if self.head is None:
            self.head = new_node 
        else:
            current = self.head 
            
            while current.next is not None:
                current = current.next 
            current.next = new_node