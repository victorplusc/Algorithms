"""
282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

Constraints:
0 <= num.length <= 10
num only contain digits.
"""
# Time complexity: O(N*4**N)
# Space complexity: O(4**N)?
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def backtrack(idx=0, path=[], val=0, prev=None):
            if idx == len(num) and val == target:
                output.append("".join(path))
                return
            
            for i in range(idx+1, len(num)+1): # we start at idx+1 so that the tmp splice has a number
                curr = num[idx:i]
                tmp = int(curr)
                if i == idx+1 or (i > idx+1 and num[idx] != "0"): # account for like 00, anything that ends with 0
                    if prev is None:
                        path.append(num[idx:i])
                        backtrack(i, path, tmp, tmp)
                        path.pop()
                    else:
                        path.append("+"+num[idx:i])
                        backtrack(i, path, val+tmp, tmp)
                        path.pop()
                        
                        path.append("-"+num[idx:i])
                        backtrack(i, path, val-tmp, -tmp)
                        path.pop()
                        
                        path.append("*"+num[idx:i])
                        backtrack(i, path, val-prev+prev*tmp, prev*tmp)
                        path.pop()
        
        output = []
        backtrack()
        return output
