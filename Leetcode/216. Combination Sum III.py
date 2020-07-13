"""
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
# Time complexity: O(2**N)
# Time complexity: O(2**N)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k, remainder, curr, idx):
            if k == 0:
                if remainder == 0:
                    output.append(curr[:])
                return
            for i in range(idx, 10):
                if i > remainder:
                    break
                curr.append(i)
                backtrack(k-1, remainder-i, curr, i+1)
                curr.pop()
                    
        output = []
        backtrack(k, n, [], 1)
        return output
