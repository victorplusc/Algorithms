"""
1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Example 4:
Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4

Example 5:
Input: nums = [0,0,0]
Output: 0

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return self.window(nums)
        return self.dp(nums)
        return self.brute_force(nums)

    # Time complexity: O(N)
    # Space complexity: O(1)
    def window(self, nums):
        best = total = start = 0
        for end, val in enumerate(nums):
            if val == 1:
                total += 1
            while start < end and total < end-start:
                if nums[start] == 1:
                    total -= 1
                start += 1
            best = max(best, end-start)
        return best

    # Time complexity: O(N)
    # Space complexity: O(N)
    def dp(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0]*n for _ in range(2)]
        
        dp[0][0] = nums[0]
        for x in range(1, n):
            if nums[x] == 1:
                dp[0][x] = dp[0][x-1] + 1
                dp[1][x] = dp[1][x-1] + 1
            elif nums[x] == 0:
                dp[0][x] = 0
                dp[1][x] = dp[0][x-1]

        return max(max(dp[0])-1, max(dp[1]))

    # Time complexity: O(N**2)
    # Space complexity: O(N**2)
    def brute_force(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        count = collections.Counter(nums)
        if count[0] == 0:
            return len(nums)-1
        elif count[1] == 0:
            return 0

        def check(arr):
            curr = 0
            highest = 0
            for val in arr:
                if val == 1:
                    curr += 1
                else:
                    highest = max(curr, highest)
                    curr = 0
            return max(curr, highest)

        backtrack = set()
        for i in range(1, n):
            if nums[i] == 0:
                backtrack.add(tuple(nums[:i] + nums[i+1:]))
        
        best = 0
        for arr in backtrack:
            best = max(best, check(arr))
        return best
        
