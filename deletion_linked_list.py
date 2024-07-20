def delete_at_start(head):
    if head is None:
        print('no element in l')
        
        return None
    new_head = head.next 
    head.next = None 
    return new_head 

# delete at end

def delete_at_end(head):
    if head is None:
        print('no element')
        
        return None 
    
    if head.next is None:
        return None 
    current = head
    
    while current.next.next is not None:
        current = current.next 
    current.next = None
    
    return head


# delete  a particular node.
def delete_at_particular(head, index):
    if head is None:
        print('no element')
        return None 
    
    if head.data == index:
        new_head = head.next 
        head.next = None
        return new_head 
    
    cureent = head 
    
    while current.next is not None and current.next.data != value:
        current = current.next 
        
    if current.next is None:
        print('value not found')
        
        return head 
    
    temp = current.next 
    current.next = current.next.next 
    temp.next = None 
    return head 