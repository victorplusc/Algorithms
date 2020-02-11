"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # return self.backtracking(digits)
        return self.iterative(digits)
    
    # Time complexity: O(3**N * 4**M)
    # Space complexity: O(3**N * 4**M)
    def backtracking(self, digits):
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        out = []
        if digits:
            self.helper("", digits, mapping, out)
        return out
    
    def helper(self, combination, next_digits, mapping, out):
        if len(next_digits) == 0:
            out.append(combination)
        else:
            for letter in mapping[next_digits[0]]:
                self.helper(combination+letter, next_digits[1:], mapping, out)
    
    # Time complexity: O(3**N * 4**M)
    # Space complexity: O(3**N * 4**M)
    def iterative(self, digits):
        if not digits: return []
        output = collections.deque()
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output.append("")
        while len(output[0]) != len(digits):
            curr = output.popleft()
            for c in mapping[digits[len(curr)]]:
                output.append(curr+c)
        return output
        
