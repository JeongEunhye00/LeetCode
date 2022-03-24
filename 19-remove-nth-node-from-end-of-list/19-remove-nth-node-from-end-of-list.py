# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = cnt = 0
        tmp = res = head
        
        while head:
            size += 1
            head = head.next
        
        while tmp:
            cnt += 1
            if size == n:
                tmp = tmp.next
                res = tmp
                break
            elif cnt == size-n:
                target = tmp.next
                tmp.next = target.next
                target.next = None
                break
            else:
                tmp = tmp.next
        
        return res