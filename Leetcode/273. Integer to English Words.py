"""
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def numberToWords(self, num: int) -> str:
        # Pad first array to account for 0, in which case we return ""
        sub20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        # We don't need the "" for tens and thousands but it allows for easy indexing
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        if num == 0:
            return "Zero"
        
        def helper(num):
            res = []
            if num < 20:
                res.append(sub20[num])
            elif num < 100:
                res.append(tens[num//10] + " " + helper(num%10))
            elif num < 1000:
                res.append(helper(num//100) + " Hundred " + helper(num%100))
            elif num < 1000000:
                res.append(helper(num//1000) + " Thousand " + helper(num%1000))
            elif num < 1000000000: # 1,000,000,000
                res.append(helper(num//1000000) + " Million " + helper(num%1000000))
            else:
                res.append(helper(num//1000000000) + " Billion " + helper(num%1000000000))
            return "".join(res).strip()
        
        return helper(num)
        
