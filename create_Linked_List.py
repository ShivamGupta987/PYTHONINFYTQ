
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
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print("None") 
        

# Example usage
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Add nodes to the linked list
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)

    # Display the linked list
    linked_list.display()
    
    
    #  for recursive print 
    def print_recursive(head):
        if head is None:
            return 
        print(head.data)
        print_recursive(head.next)
        
# rewrite

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
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print("None") 
        

# Example usage
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Add nodes to the linked list
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)

    # Display the linked list
    linked_list.display()
    
    
    #  for recursive print 
    def print_recursive(head):
        if head is None:
            return 
        print(head.data)
        print_recursive(head.next)