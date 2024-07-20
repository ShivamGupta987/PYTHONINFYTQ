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
    
    ll.display()
