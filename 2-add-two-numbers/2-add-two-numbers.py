# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode()
        carry = 0

        while l1 != None or l2 != None:
            val1 = val2 = 0
            if l1: val1 = l1.val
            if l2: val2 = l2.val
            
            n1 = val1 + val2 + carry
            
            carry = n1 // 10
        
            dummy.next = ListNode(n1%10)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(carry)

        return res.next