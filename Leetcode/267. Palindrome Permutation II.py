"""
267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
"""
# Time complexity: O((N/2+1)!)
# Space complexity: O(N)
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        output = []
        counter = collections.Counter(s)
        odd = [key for key, val in counter.items() if val % 2 != 0]
        if len(odd) > 1:
            return []
        if len(odd) == 1:
            counter[odd[0]] -= 1
            self.helper(odd[0], counter, output, n)
        else:
            self.helper("", counter, output, n)
        return output

    def helper(self, curr, counter, output, n):
        if len(curr) == n:
            output.append(curr)
            return
        for key, val in counter.items():
            if val > 0:
                counter[key] -= 2
                self.helper(key + curr + key, counter, output, n)
                counter[key] += 2
