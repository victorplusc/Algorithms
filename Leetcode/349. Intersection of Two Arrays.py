#349. Intersection of Two Arrays
"""
Given two arrays, write a function to compute their intersection.
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        #nums 1 is shorter
        
        elements1 = set(nums1)
        elements2 = {element for element in nums2 if element in elements1}
        
        return list(elements2)
