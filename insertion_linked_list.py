class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def insert_at_pos(self, data, position):
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for i in range(1, position - 1):
            if current is None:
                print("Invalid position")
                return self.head
            current = current.next
        
        if current is None:
            print("Invalid position")
            return self.head
        
        new_node.next = current.next
        current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example usage:
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(1)
    ll.insert_at_end(100)
    ll.insert_at_pos(50, 3)
    
    ll.display()
