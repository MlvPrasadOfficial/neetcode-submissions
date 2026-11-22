# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        ans = ListNode()
        dummy = ans 
        e = 0 #carry
        m = 0 
        dd = []
        ee = []
        z = 0 
        sp = 0
        while l1 or l2 or e :          
            z+=1
            if l1 : a = l1.val
            else  : a = 0 

            if l2 : b = l2.val
            else  : b = 0             
            print(a,b)
            c = a + b  # 9 + 0
            d = c % 10 # 8
            print("+++",c,d)

                # break
            if  e == 1 :
                d = d + 1
                if d == 10 : 
                    d = 0 
                    e = 1
                    sp = 1
                    print("sp")
          
            
            ans.next = ListNode(d) # 8
            if sp == 1 :                
                e = 1
                sp  = 0
            else : 
                e= c // 10 
            
            dd.append(d)
            ee.append(e)
            print(dd,ee)
            print()    

            
            ans = ans.next
            if l1 :  l1 = l1.next
            if l2 : l2 = l2.next
            # if z == 10:  break
        return dummy.next


        # 
        