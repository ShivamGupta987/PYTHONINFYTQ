# reverse the queue


from collections import deque

def reverse_queue(q):
    stack = []
    
    while q:
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())
        
    return q

queue = reverse_queue(deque([1,2,3,4,5]))
print(queue)


# remove even form queue


from collections import deque

def remove(q):
    
    temp_queue = deque()
    index = 0 
    
    while q:
        element = q.popleft()
        
        if index!=0:
            temp_queue.append(element)  
            
        index+=1 
    return temp_queue 


q = deque([1,2,3,4,5]) 
result_queue = remove_position(q)
    
print( list(result_queue))




