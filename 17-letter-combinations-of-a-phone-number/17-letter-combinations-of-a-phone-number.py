class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def numberOfCases(ch, s_list):
            answer = []
            for i in range(len(s_list)):
                answer.append(ch + s_list[i])
            return answer
        
        
        d = {2:["a", "b", "c"], 3:["d", "e", "f"], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'],
            6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        answer = list()
        
        for i in range(len(digits)-1, -1, -1):
            if int(digits[i]) != 1:
                if i == len(digits)-1:
                    answer = numberOfCases("", d[int(digits[i])])
                else:
                    tmp = list()
                    for ch in d[int(digits[i])]:
                        tmp += numberOfCases(ch, answer)
                    answer = tmp
        return answer