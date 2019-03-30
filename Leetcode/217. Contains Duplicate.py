"""Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False

    #Time complexity: O(N)
    #Space complexity: O(N)
