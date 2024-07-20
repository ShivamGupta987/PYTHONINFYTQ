#83 question on leetcode remove duplicates
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next 

        while fast!=None:
            if slow.val == fast.val:
                slow.next = fast.next 

            else:
                slow = slow.next
            fast = fast.next
        return head
    
# ROATATE LIST LEETCODE 61 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head 

        # length 
        length = 1 
        tail = head 
        while tail.next:
            tail=tail.next 
            length+=1 

        # update k 
        k = k%length

        if k == 0:
            return head 

        #new head 
        new_tail = head 
        for i in range(length-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        tail.next = head 
        new_tail.next = None

        return new_head
        