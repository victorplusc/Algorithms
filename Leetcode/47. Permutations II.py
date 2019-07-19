"""
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
"""
# Time complexity: O(N*N)
# Space complexity: O(N*N)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        observed = set()
        self.permute_helper(nums, [], observed)
        permutations = [[j for j in i] for i in observed]
        return permutations

    def permute_helper(self, nums: List[int], current: List[int], observed):
        if nums == []:
            observed.add(tuple(current))
        else:
            for i, num in enumerate(nums):
                curr_num = num
                del(nums[i])
                current.append(curr_num)
                self.permute_helper([i for i in nums], [j for j in current], observed)
                nums.insert(i, curr_num)
                del(current[-1])
        
