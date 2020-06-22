"""
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False

Constraints:
1 <= nums.length <= 10000
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tails = collections.Counter()
        for val in nums:
            if not count[val]: continue
            count[val] -= 1
            if tails[val - 1] > 0:
                tails[val - 1] -= 1
                tails[val] += 1
            elif count[val + 1] and count[val + 2]:
                count[val + 1] -= 1
                count[val + 2] -= 1
                tails[val + 2] += 1
            else:
                return False
        return True
