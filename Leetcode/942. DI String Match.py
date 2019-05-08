# 942. DI String Match

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        vals = list(range(len(S)))
        left = right = 0
        arr = []
        
        for i, char in enumerate(S):
            if char == "I":
                if arr == []:
                    arr.append(0)
                    left += 1
                else:
                    arr.append(vals[left])
                    left += 1
            if char == "D":
                if arr == []:
                    arr.append(vals[-1]+1)
                    right += 1
                else:
                    arr.append(vals[-1-right])
                    right += 1
        
        if S[-1] == "I":
            arr.append(vals[left])
        else:
            arr.append(vals[right])
        
        return arr
