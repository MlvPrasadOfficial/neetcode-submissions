# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        print(dummy.val)
        print(node.val)

        while list1 and list2:
            print(list1.val,list2.val)
            if list1.val < list2.val:
                node.next = list1
                print("-|-",node.next.val)
                list1 = list1.next
            else:
                node.next = list2
                print("--",node.next.val)
                list2 = list2.next
            node = node.next
            print("d",dummy.val)
            print("n",node.val)
            print()
        node.next = list1 or list2

        return dummy.next