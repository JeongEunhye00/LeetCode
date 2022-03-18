class Solution:
    def reverse(self, x: int) -> int:
        neg_num = False
        if x<0:
            neg_num = True
            x = x*-1
        x = str(x)    
        res = 0
        for i in range(len(x)):
            res += int(x[-1-i])*(10**(len(x)-1-i))
        
        res = int(res)
        if neg_num:
            res *= -1
        
        if (2**31 * -1) <= res <= (2**31 -1):
            return res
        else:
            return 0