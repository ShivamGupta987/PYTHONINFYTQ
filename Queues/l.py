class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 
        
    def is_empty(self):
        return self.front is None 
    
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node 
            
        self.rear.next = new_node 
        self.rear = new_node 
        
        
    def dequeue(self):
        if self.is_empty():
            return None 
        
        temp = self.front 
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data 
    
    def print_queue(self):
        temp  =self.front 
        
        
        while temp:
            print(temp.data,end = "")
            
            temp = temp.next 
        print()      
        
        
if __name__ == '__main__':
    queue = Queue()


    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("Queue:")
    queue.print_queue()

    # Dequeue elements and print
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())

    print("Queue after dequeue:")
    queue.print_queue()  
        