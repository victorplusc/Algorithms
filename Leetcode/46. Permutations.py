"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.
"""
# Time complexity: O(N!)
# Space complexity: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(start):
            if start == n:
                output.append(nums[:])
            else:
                for i in range(start, n):
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]
        output = []
        backtrack(0)
        return output
