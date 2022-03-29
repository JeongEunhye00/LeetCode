class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list()
        digits[-1] += 1
        carry = 0
        
        for num in digits[-1::-1]:
            res.insert(0, (num+carry)%10)
            
            if (num+carry) // 10 == 1: carry = 1
            else: carry = 0
            
        if carry:
            res.insert(0, 1)
        
        return res