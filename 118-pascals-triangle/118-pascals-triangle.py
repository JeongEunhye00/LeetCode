class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nthRow(prevRow):
            prev = prevRow[:]
            prev.insert(0,0)
            prev.append(0)
            
            res = list()
            for i in range(len(prev)-1):
                res.append(prev[i]+prev[i+1])
                
            return res
        
        pascal = list()
        
        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            else:
                pascal.append(nthRow(pascal[-1]))
        
        return pascal