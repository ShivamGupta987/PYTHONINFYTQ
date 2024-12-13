# leetcode 876 problem easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        length = 1 
        current = head
        while current.next is not None:
            current = current.next
            length+=1
        middle = length//2 
        while middle:
            head = head.next
            middle-=1 
        return head
    
    
# leetcode problem 160 solved 
# method1 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        data = set()
        current = headA 
        while current:
            data.add(current)
            current = current.next 

        current = headB 
        while current:
            if current in data:
                return current
            current = current.next 

        return None
#  method 2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA,lenB = 1,1 
        currA,currB = headA,headB 

        while currA.next:
            lenA+=1
            currA = currA.next
        while currB.next:
            lenB+=1
            currB = currB.next

        diff = abs(lenA - lenB)

        if lenA > lenB:
            while diff:
                headA = headA.next 
                diff-=1 
        if lenB > lenA:
            while diff:
                headB = headB.next 
                diff-=1 

        while(headA!=headB):
            headA = headA.next
            headB = headB.next

        return headA



# problem 21 leetcode merged two sorted list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 

            tail = tail.next 

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
    
    # leetcodd problem 148 sort list 
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Function to split the linked list into two halves
        def split(head):
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None  
            return head, slow
        
 
        def merge(left, right):
            dummy = ListNode()
            current = dummy
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left if left else right
            return dummy.next
        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
    
    # 2nd method
    
    # middle element
    
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def middle_element(head):
    if not head:
        return head
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge_two_list(left, right):
    dummy = ListNode()
    tail = dummy
    
    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    if left:
        tail.next = left
    if right:
        tail.next = right
    
    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = middle_element(head)
    
    # Break the list into two halves
    next_to_mid = mid.next
    mid.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_mid)
    
    # Merge the sorted halves
    sorted_list = merge_two_list(left, right)
    
    return sorted_list

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))

# Test the merge_sort function
if __name__ == "__main__":
    # Create an unsorted linked list
    values = [4, 2, 1, 3]
    head = create_linked_list(values)
    
    print("Original linked list:")
    print_linked_list(head)
    
    # Sort the linked list
    sorted_head = merge_sort(head)
    
    print("Sorted linked list:")
    print_linked_list(sorted_head)

        
        
        
        
            

# rewrite

# leetcode 876 problem easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        length = 1 
        current = head
        while current.next is not None:
            current = current.next
            length+=1
        middle = length//2 
        while middle:
            head = head.next
            middle-=1 
        return head
    
    
# leetcode problem 160 solved 
# method1 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        data = set()
        current = headA 
        while current:
            data.add(current)
            current = current.next 

        current = headB 
        while current:
            if current in data:
                return current
            current = current.next 

        return None
#  method 2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA,lenB = 1,1 
        currA,currB = headA,headB 

        while currA.next:
            lenA+=1
            currA = currA.next
        while currB.next:
            lenB+=1
            currB = currB.next

        diff = abs(lenA - lenB)

        if lenA > lenB:
            while diff:
                headA = headA.next 
                diff-=1 
        if lenB > lenA:
            while diff:
                headB = headB.next 
                diff-=1 

        while(headA!=headB):
            headA = headA.next
            headB = headB.next

        return headA



# problem 21 leetcode merged two sorted list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 

            tail = tail.next 

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
    
    # leetcodd problem 148 sort list 
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Function to split the linked list into two halves
        def split(head):
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None  
            return head, slow
        
 
        def merge(left, right):
            dummy = ListNode()
            current = dummy
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left if left else right
            return dummy.next
        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
    
    # 2nd method
    
    # middle element
    
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def middle_element(head):
    if not head:
        return head
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge_two_list(left, right):
    dummy = ListNode()
    tail = dummy
    
    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    if left:
        tail.next = left
    if right:
        tail.next = right
    
    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = middle_element(head)
    
    # Break the list into two halves
    next_to_mid = mid.next
    mid.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_mid)
    
    # Merge the sorted halves
    sorted_list = merge_two_list(left, right)
    
    return sorted_list

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))

# Test the merge_sort function
if __name__ == "__main__":
    # Create an unsorted linked list
    values = [4, 2, 1, 3]
    head = create_linked_list(values)
    
    print("Original linked list:")
    print_linked_list(head)
    
    # Sort the linked list
    sorted_head = merge_sort(head)
    
    print("Sorted linked list:")
    print_linked_list(sorted_head)

        
        
        
        
            

   