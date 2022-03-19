class Solution:
    def convert(self, s: str, numRows: int) -> str:
        idx = [0]*len(s)
        k = 1
        res = ""
        if numRows == 1:
            return s
        d = dict()
        for i in range(numRows):
            d[i] = list()

        for i in range(len(s)):
            if i != 0:
                idx[i] = idx[i-1] + k
                if idx[i] == numRows-1:
                    k = -1
                if idx[i] == 0:
                    k = 1
            d[idx[i]].append(i)

        for i in range(numRows):
            for j in d[i]:
                res += s[j]
                
        return res