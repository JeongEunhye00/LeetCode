class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, c_res = 0, 0
        chk = list()
        
        for i in list(s):                
            if i not in chk:
                c_res += 1
                chk.append(i)
            else:
                chk = chk[chk.index(i)+1:]
                chk.append(i)
                c_res = len(chk)
            
            if c_res > res:
                res = c_res
            
        return res