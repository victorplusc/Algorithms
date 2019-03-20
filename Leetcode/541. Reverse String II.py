"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        newStr = []
        temp = []
        step = 0
        
        for i, x in enumerate(s):
            
            if step < k:
                temp.insert(0,x)
                step += 1
            elif step <= 2*k:
                temp.append(x)
                step += 1
            else:
                step += 1
            if step == 2*k or i == len(s)-1:
                newStr.append("".join(temp))
                step = 0
                temp = []

        return "".join(newStr)
