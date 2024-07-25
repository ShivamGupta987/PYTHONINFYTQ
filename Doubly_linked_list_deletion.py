class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None
        
class Doubly_Linked_List:
    def __init__(self):
        self.head = None 
        
        #  at start 
        
    def delete_at_start(self):
        if self.head is None:
            return None        
        if self.head.next is None:
            self.head = None 
            
        else:
            self.head = self.head.next
            self.head.prev = None 
            
    # at end 
    
    def delete_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None: 
            self.head = None
            
        else:
            temp = self.head
            
            while temp.next is not None:
                temp = temp.next 
            temp.prev.next = None 
            
    # at specific position 
    
    def delete_at_position(self,data):
        if self.head is None:
            return None 

        temp = self.head
        
        while temp is not None:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next 
                if temp.next:
                    temp.next.prev = temp.prev
                    
                if temp == self.head:
                    self.head = temp.next 
                break 
            temp = temp.next

                    
                
                    
                
        
        
                
            