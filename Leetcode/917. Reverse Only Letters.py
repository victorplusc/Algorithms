"""
917. Reverse Only Letters
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
# Time complexity: O(N)
# Space complexity: O(1) if S is mutable else O(N)
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        mutable_s = list(S)
        alphabet = {chr(i+ord('a')) for i in range(26)} | {chr(i+ord('A')) for i in range(26)}
        i = 0
        j = len(S)-1
        while i < j:
            if mutable_s[i] not in alphabet:
                i += 1
            elif mutable_s[j] not in alphabet:
                j -= 1
            else:
                mutable_s[i], mutable_s[j] = mutable_s[j], mutable_s[i]
                i += 1
                j -= 1
        return "".join(mutable_s)
