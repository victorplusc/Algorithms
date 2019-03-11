class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occurrences = {}
        
        for i in range(len(s)-9):
            new = (s[i:i+10])
            
            if new not in occurrences:
                occurrences[new] = False
            else:
                occurrences[new] = True
            
        return ([i for i in occurrences if occurrences[i] == True])
