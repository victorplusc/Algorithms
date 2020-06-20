"""
Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
"""
# Time complexity: O(N**2)
# Space complexity: O(N)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ["1"]
        
        for i in range(1, n):
            factorials.append(factorials[i-1] * i)
            nums.append(str(i+1))
            
        k -= 1
        output = []
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            output.append(nums[idx])
            del nums[idx]
        
        return "".join(output)
