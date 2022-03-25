# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    dummy.next = ListNode(list1.val)
                    dummy, list1 = dummy.next, list1.next
                else:
                    dummy.next = ListNode(list2.val)
                    dummy, list2 = dummy.next, list2.next
            
            if list1 and not list2:
                dummy.next = ListNode(list1.val)
                dummy, list1 = dummy.next, list1.next
            
            if not list1 and list2:
                dummy.next = ListNode(list2.val)
                dummy, list2 = dummy.next, list2.next
                
        return res.next