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
        if not num:
            return "Zero"
        billions = num // 1000000000
        millions = (num-billions*1000000000) // 1000000
        thousands = (num - billions*1000000000 - millions*1000000) // 1000
        rem = (num - billions*1000000000 - millions*1000000 - thousands*1000)
        
        output = []
        if billions:
            output.append(self.three(billions) + " Billion")
        
        if millions:
            if output: output.append(" ")
            output.append(self.three(millions) + " Million")
        
        if thousands:
            if output: output.append(" ")
            output.append(self.three(thousands) + " Thousand")
            
        if rem:
            if output: output.append(" ")
            output.append(self.three(rem))
        
        return "".join(output)
    
    def three(self, num):
        hundreds = num//100
        rem = num-hundreds*100
        if hundreds and rem:
            return self.one(hundreds) + " Hundred " + self.two(rem)
        elif not hundreds and rem:
            return self.two(rem)
        elif hundreds and not rem:
            return self.one(hundreds) + " Hundred"
    
    def two(self, num):
        if not num:
            return ""
        elif num < 10:
            return self.one(num)
        elif num < 20:
            return self.sub_20(num)
        else:
            tens = num // 10
            rem = num - tens*10
            return self.ten(tens) + " " + self.one(rem) if rem else self.ten(tens)
    
    def ten(self, num):
        mapping = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        return mapping[num]
    
    def sub_20(self, num):
        mapping = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        return mapping[num]
    
    def one(self, num):
        mapping = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        return mapping[num]
