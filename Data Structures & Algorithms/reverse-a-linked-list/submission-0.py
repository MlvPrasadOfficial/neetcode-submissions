# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None ,head

        # pc  01 
        # temp 2
        # c = 0 

        while c :
            temp = c.next
            c.next = p
            p = c
            c = temp
        return p

        