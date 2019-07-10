"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        outer_indices = set()
        count = 0
        for i, char in enumerate(S):
            if char == "(":
                if count == 0:
                    outer_indices.add(i)
                count += 1
            else:
                count -= 1
                if count == 0:
                    outer_indices.add(i)
            
        string_builder = []
        for i, char in enumerate(S):
            if i not in outer_indices:
                string_builder.append(char)
        return "".join(string_builder)
