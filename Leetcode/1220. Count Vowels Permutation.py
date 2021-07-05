"""
1220. Count Vowels Permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 
Input: n = 5
Output: 68

Constraints:
1 <= n <= 2 * 10^4
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a_end = e_end = i_end = o_end = u_end = 1
        
        for i in range(n-1):
            a_end_new = (e_end + i_end + u_end)
            e_end_new = (a_end + i_end)
            i_end_new = (e_end + o_end)
            o_end_new = (i_end)
            u_end_new = (i_end + o_end)
            
            a_end, e_end, i_end, o_end, u_end = a_end_new, e_end_new, i_end_new, o_end_new, u_end_new
        
        return (a_end + e_end + i_end + o_end + u_end)%(10**9 + 7)
