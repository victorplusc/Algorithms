"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""
# Time complexity: O(N*2**N)
# Space complexity: O(2**N)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        res = []
        
        def is_valid(candidate):
            opening = 0
            for c in candidate:
                if c == "(":
                    opening += 1
                elif c == ")":
                    if opening == 0:
                        return False
                    opening -= 1
            return opening == 0
        
        seen = {s}
        q = collections.deque([s])
        
        found = False
        while q:
            front = q.popleft()
            if is_valid(front):
                res.append(front)
                found = True
            
            if found: continue
                
            for i, c in enumerate(front):
                if c != "(" and c != ")": continue
                
                candidate = front[0:i] + front[i+1:]
                if candidate not in seen:
                    q.append(candidate)
                    seen.add(candidate)
        return res
        
        
