class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch = ['(', ')', '{', '}', '[', ']']
        for k in s:
            stack.append(k)
            if k in ch[1::2] and len(stack) > 1:
                chk_close = ch.index(stack[-1]) - ch.index(stack[-2])
                if chk_close == 1:
                    stack.pop()
                    stack.pop()
        if not stack:
            return True
        else:
            return False
                
                