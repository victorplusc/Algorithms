"""
784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
# Time complexity: O(2^N * N)
# Space complexity: O(2^N * N)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        permutations = []
        self.backtrack(permutations, 0, [c for c in S])
        return permutations
    
    def backtrack(self, perms, i, S):
        if i == len(S):
            perms.append("".join(S))
        else:
            if S[i].isalpha():
                S[i] = S[i].upper()
                self.backtrack(perms, i+1, S)
                S[i] = S[i].lower()
                self.backtrack(perms, i+1, S)
            else:
                self.backtrack(perms, i+1, S)
