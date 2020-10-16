"""
689. Maximum Sum of 3 Non-Overlapping Subarrays
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""
# Time complexity: O(N)
# Space complexity: O(1)
"""
Algorithm

1) Initialize:
    # DEPENDS ON RETURN OBJECTIVE:
    i. single best left index
    ii. best two leftmost indices
    iii. best three indices (because this is what is returned)
    
2) Initialize three rolling sums
3) Initialize three variables representing best sums from left to right
4) Initialize pointers at 1, k+1, k*2+1 (after first step)
5) While right is in range, move all window sums and update best sum values
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # indices where our best sequences begin
        best_left = 0
        best_two_indices = [0, k]
        best_three_indices = [0, k, k*2]
        
        left_sum = sum(nums[0:k])
        mid_sum = sum(nums[k:k*2])
        right_sum = sum(nums[k*2:k*3])
        
        best_1_sum = left_sum
        best_2_sum = left_sum + mid_sum # from left to right
        best_3_sum = left_sum + mid_sum + right_sum
        
        # initialize pointers after first step has been done
        left, mid, right = 1, k+1, k*2+1
        while right <= len(nums)-k:
            left_sum = left_sum - nums[left-1] + nums[left+k-1]
            mid_sum = mid_sum - nums[mid-1] + nums[mid+k-1]
            right_sum = right_sum - nums[right-1] + nums[right+k-1]
            
            if left_sum > best_1_sum:
                best_left = left
                best_1_sum = left_sum
                
            if best_1_sum + mid_sum > best_2_sum:
                best_two_indices = [best_left, mid]
                best_2_sum = best_1_sum + mid_sum
            
            if best_2_sum + right_sum > best_3_sum:
                best_three_indices = best_two_indices + [right]
                best_3_sum = best_2_sum + right_sum
            
            left += 1
            mid += 1
            right += 1
        return best_three_indices
