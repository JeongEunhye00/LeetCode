# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            res = head.next
        
        chk = False
        while head:
            tmp = head
            next = head.next

            if next:
                head.next = next.next
                next.next = tmp
                if chk:
                    prev.next = next
                chk = True
            
            prev = tmp
            head = head.next

        return res