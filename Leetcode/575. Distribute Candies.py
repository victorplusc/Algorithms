"""
575. Distribute Candies
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candy_set = {candy for candy in candies}
        return min(len(candy_set), len(candies)//2)
