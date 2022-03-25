class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = list()
        
        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            else:
                tmp = [0] + pascal[-1] + [0]
                nth = list()
                for j in range(len(tmp)-1):
                    nth.append(tmp[j]+tmp[j+1])
                pascal.append(nth)
        
        return pascal