"""
1060. Missing Element in Sorted Array
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:
1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # return self.naive(nums, k)
        return self.binary_search(nums, k)
    
    # Time complexity: O(log N)
    # Space complexity: O(1)
    def binary_search(self, nums, k):
        n = len(nums)
        missing = lambda x: nums[x] - nums[0] - x
        
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)
        
        left, right = 0, n-1
        
        while left < right:
            mid = (left+right)//2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[right-1] + k - missing(right-1)
        
    # Time complexity: O(N)
    # Space complexity: O(1)
    def naive(self, nums, k):
        n = len(nums)
        missing = lambda x: nums[x] - nums[0] - x
        
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)
        
        idx = 1
        while missing(idx) < k:
            idx += 1
        
        return nums[idx-1] + k - missing(idx-1)
    
