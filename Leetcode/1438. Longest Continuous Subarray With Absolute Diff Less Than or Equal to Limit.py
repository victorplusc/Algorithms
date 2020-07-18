"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # return self.two_heaps(nums, limit)
        return self.two_deques(nums, limit)
    
    def two_deques(self, nums, limit):
        max_q = collections.deque()
        min_q = collections.deque()
        i = 0
        longest = 0
        for j, n in enumerate(nums):
            while max_q and n > max_q[-1]: max_q.pop()
            while min_q and n < min_q[-1]: min_q.pop()
            max_q.append(n)
            min_q.append(n)
            if max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[i]: max_q.popleft()
                if min_q[0] == nums[i]: min_q.popleft()
                i += 1
            else:
                longest = max(longest, j-i+1)
        return longest
    
    def two_heaps(self, nums, limit):
        longest = 0
        start = 0
        min_heap = []
        max_heap = []
        for end, n in enumerate(nums):
            heapq.heappush(max_heap, [-n, end])
            heapq.heappush(min_heap, [n, end])
            while -max_heap[0][0] - min_heap[0][0] > limit:
                start = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < start:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < start:
                    heapq.heappop(min_heap)
            longest = max(longest, end-start+1)
        return longest
