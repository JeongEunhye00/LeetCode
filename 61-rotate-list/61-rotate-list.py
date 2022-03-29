# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        
        start = prev = head
        n = 0
        size = 1
        cnt = 1
            
        while n != cnt:
            while head:
                if head.next == None:
                    if n == 0: cnt = k % size
                    if cnt == 0: return start
                    n += 1
                    head.next = start
                    prev.next = None
                    start = head
                    break
                else:
                    if n == 0: size += 1
                    prev = head
                    head = head.next
            if size == 1: break
                    
        return start