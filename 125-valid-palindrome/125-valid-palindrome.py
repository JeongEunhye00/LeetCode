class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        i = 0
        while i != len(s):
            if s[i].isalnum():
                i += 1
            else:
                s = s[:i] + s[i+1:]
        
        if s == "".join(reversed(s)):
            return True
        else:
            return False