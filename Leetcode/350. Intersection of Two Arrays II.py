#350. Intersection of Two Arrays II
"""
Given two arrays, write a function to compute their intersection.

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        dict1 = dict()
        dict2 = dict()
        
        for c in nums1:
            dict1[c] = dict1.get(c, 0) + 1
        
        for c in nums2:
            dict2[c] = dict2.get(c, 0) + 1
            if dict1 == dict2:
                break
        
        intersection = []
        
        for item in dict1:
            for i in range(min(dict1[item], dict2.get(item, 0))):
                intersection.append(item)
        
        return intersection

"""
If sorted:
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i = 0
        j = 0
        
        intersection
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+= 1
            else:
                j+= 1
        
        return intersection
