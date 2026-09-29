# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None 

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 

        l1,l2 = head, prev
        while l2:

            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2






     


        
        
        




        