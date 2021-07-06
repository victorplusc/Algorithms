"""
1338. Reduce Array Size to The Half
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:
Input: arr = [1,9]
Output: 1

Example 4:
Input: arr = [1000,1000,3,7]
Output: 1

Example 5:
Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5

Constraints:
1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter()
        max_freq = 0
        
        for val in arr:
            counter[val] += 1
            max_freq = max(max_freq, counter[val])
        
        bucket = collections.defaultdict(int)
        
        for val, freq in counter.items():
            bucket[freq] += 1
            
        size = len(arr)
        deletions = 0
        while size > len(arr)//2:
            for i in range(bucket[max_freq]):
                size -= max_freq
                deletions += 1
                if size <= len(arr)//2:
                    return deletions
            max_freq -= 1
        return deletions
