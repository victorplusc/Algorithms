"""
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.binary_search(nums, m)
        return self.dp(nums, m)
    
    # Time complexity: O(N*log(sum(A)))
    # Space complexity: O(N)
    def binary_search(self, nums, m):
        def is_valid(mid):
            cuts = curr_sum = 0
            for val in nums:
                curr_sum += val
                if curr_sum > mid:
                    cuts += 1
                    curr_sum = val
            return cuts+1 <= m
        
        low, high, best = max(nums), sum(nums), -1
        
        while low <= high:
            mid = (low+high)//2
            if is_valid(mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best
    
    # Time complexity: O(N**2*M)
    # Space complexity: O(N*M)
    def dp(self, nums, m):
        n = len(nums)
        f = [[float('inf')]*(m+1) for _ in range(n+1)]
        sub = [0]*(n+1)
        
        for i in range(n):
            sub[i+1] = sub[i] + nums[i]
        
        f[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i]-sub[k]))

        return f[n][m]
