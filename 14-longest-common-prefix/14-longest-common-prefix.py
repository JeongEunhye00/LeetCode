class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""
        if len(strs) == 1:
            return strs[0]
        
        elif "" in strs:
            return ""
        
        else:
            str1 = strs[0]
            for k in range(1, len(strs)):
                str2 = strs[k]
                if len(str1) > len(str2):
                    str1, str2 = str2, str1
                for i in range(len(str1), 0, -1):
                    if str2.startswith(str1[0:i]):
                        res = str1[0:i]
                        str1 = res
                        break
                    else:
                        res =""
                if res == "":
                    break
                
        return res