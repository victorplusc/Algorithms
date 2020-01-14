"""
548. Split Array with Equal Sum
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
"""
# Time complexity: O(N**2)
# Space complexity: O(N)
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        left_sum = [0]
        for n in nums: 
            left_sum.append(left_sum[-1] + n)

        n = len(nums)
        d = collections.defaultdict(list)
        for i, v in enumerate(left_sum):
            d[v].append(i)

        for j in range(1, n-1):
            for k in range(j+1, n-1):
                for i in d[left_sum[-1] - left_sum[k+1]]:
                    if i >= j: 
                        break
                    if left_sum[i] == left_sum[j] - left_sum[i+1] == left_sum[k] - left_sum[j+1]:
                        return True
        return False
