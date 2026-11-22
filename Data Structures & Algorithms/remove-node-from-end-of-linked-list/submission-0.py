# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head) # extra 0 
        left = dummy # referencing
        right = head # actual

        while n > 0 :
            right = right.next 
            n = n-1 # move n steps it is n+1 from start

        while right :               # lets n=3 , in 10 values 7 value 
            left  = left.next       # should be remove , 
            right = right.next      # so if right is on 11
                                    # then next should be 6 no 7 can be skipped
            
        left.next = left.next.next # skip 7 and connect to 0 

        # but we also want skip 0 in dummy
        return dummy.next
                                     
                                    

        
