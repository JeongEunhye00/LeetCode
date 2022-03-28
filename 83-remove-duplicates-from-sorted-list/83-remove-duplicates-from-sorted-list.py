# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        
        while head:
            next = head.next
            if next and head.val == next.val:
                head.next = next.next
                next.next = None
            else:
                head = head.next
        
        return res