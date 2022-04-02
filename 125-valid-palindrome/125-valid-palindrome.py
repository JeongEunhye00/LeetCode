class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
                
        if res == res[::-1]:
            return True
        else:
            return False