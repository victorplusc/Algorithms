"""
809. Expressive Words
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""
# Time complexity: O(W*K)
# Space complexity: O(K)
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return sum(self.check(S, w) for w in words)
    
    def check(self, s, w):
        j, n, m = 0, len(s), len(w)
        for i in range(n):
            if j < m and s[i] == w[j]:
                j += 1
            elif s[i-1:i+2] != s[i] * 3 and s[i] * 3 != s[i-2:i+1]: return False
        return j == m
    
    def check2(self, s, w):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(s), len(w)
        while i < n and j < m:
            if s[i] != w[j]: return False
            while i2 < n and s[i2] == s[i]: i2 += 1
            while j2 < m and w[j2] == w[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
        return i == n and j == m

