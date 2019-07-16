"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.
"""
# Time complexity: O(N*N)
# Space complexity: O(N*N)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.recursive_helper(permutations, nums, [])
        return permutations
    
    def recursive_helper(self, permutations, nums, current):
        if nums == []:
            permutations.append(current)
        else:
            for i in range(len(nums)):
                current_num = nums[i]
                current.append(current_num)
                nums.remove(current_num)
                self.recursive_helper(permutations, [i for i in nums], [j for j in current])
                nums.insert(i, current_num)
                current.remove(current_num)
