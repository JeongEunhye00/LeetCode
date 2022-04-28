class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        res_str = ""
        neg = False
        
        if s == "":
            return 0
        else:
            if s[0] in ['+', '-'] or s[0].isdigit():
                for i in range(len(s)):
                    if s[i] == '-':
                        neg = True
                    elif s[i].isdigit():
                        res_str += s[i]
                    if (i != len(s)-1) and (not s[i+1].isdigit()):
                        break

            if res_str:
                if neg:
                    res = max(-1*(2**31), -1*int(res_str))
                else:
                    res = min(int(res_str), (2**31)-1)
            else:
                res = 0

            return res