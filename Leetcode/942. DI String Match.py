# 942. DI String Match

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        vals = list(range(len(S)+1))
        left = right = 0
        arr = []
        
        for i, char in enumerate(S):
            if char == "I":
                arr.append(vals[left])
                left += 1
            if char == "D":
                arr.append(vals[-1-right])
                right += 1
        
        arr.append(vals[left])
        
        return arr
    
# Time complexity: O(N)
# Space complexity: O(N)
