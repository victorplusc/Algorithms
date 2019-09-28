"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
from collections import deque

class Solution(object):
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left = [0 for _ in nums]
        left[0] = nums[0]
        
        right = [0 for _ in nums]
        right[-1] = nums[-1]
        
        for i in range(1, n):
            if i%k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        
        output = []
        for i in range(n-k+1):
            output.append(max(left[i+k-1], right[i]))
            
        return output
        
    
    # Time complexity: O(N*k)
    # Space complexity: O(N-k)
    def hammer_sliding_window(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        indices = []
        for i in range(n-k+1):
            indices.append(max(nums[i:i+k]))
        
        return indices
    
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def deque_sliding_window(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        q = deque()
        max_index = 0
        for i in range(k):
            self.clean_deque(nums, q, k, i)
            q.append(i)
            if nums[i] > nums[max_index]:
                max_index = i
        output = [nums[max_index]]
        
        for i in range(k, n):
            self.clean_deque(nums, q, k, i)
            q.append(i)
            output.append(nums[q[0]])
        return output
        
    def clean_deque(self, nums, q, k, i):
        if q and q[0] == i-k:
            q.popleft()
        
        while q and nums[i]>nums[q[-1]]:
            q.pop()
