class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None
class DoublyLinkedList : 
    def __init__(self):
        self.head = None 
    # at start add 
    def insert_at_start(self,data):
        # new node creating
        new_node = Node(data)
        if self.head == None:
            # agr headnone hai toh apna head ihi new node hoga
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
            
    # at the end 
    
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node 
        else:
            temp = self.head 
            # loop use rkenge ki kb head none hoga jaise noene hua head (temp) ka next usse new node de denge aur uska previous temp
            
            while temp.next is not None:
                temp = temp.next 
                
            temp.next = new_node 
            new_node.prev = temp

    
    # at specific position 
    
    def insert_At_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_start(data)
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
                if temp is None:
                    print("position is out of range")
                    
            new_node.next = temp.next 
            new_node.prev = temp 
            # agr temp next hai toh uska prev new nod eho jyega
            if temp.next:
                temp.next.prev = new_node
                
            temp.next = new_node
                
            

                
        
            
            
    