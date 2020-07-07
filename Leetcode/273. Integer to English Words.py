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
        millions = (num%1000000000)//1000000
        thousands = (num%1000000000%1000000) // 1000
        remainder = (num%1000000000%1000000%1000)
        
        output = []
        if billions:
            output.append(self.process_hundreds(billions) + " Billion")
            
        if millions:
            if output: output.append(" ")
            output.append(self.process_hundreds(millions) + " Million")
        
        if thousands:
            if output: output.append(" ")
            output.append(self.process_hundreds(thousands) + " Thousand")
            
        if remainder:
            if output: output.append(" ")
            output.append(self.process_hundreds(remainder))
        
        return "".join(output)
    
    def process_hundreds(self, num):
        hundreds = num//100
        remainder = num%100
        if hundreds and remainder:
            return self.process_single(hundreds) + " Hundred " + self.process_double(remainder)
        if hundreds and not remainder:
            return self.process_single(hundreds) + " Hundred"
        if not hundreds and remainder:
            return self.process_double(remainder)
        
    def process_double(self, num):
        if not num: return ""
        elif num < 10:
            return self.process_single(num)
        elif num < 20:
            return self.process_sub_20(num)
        else:
            tens = num//10
            remainder = num%10
            return self.process_tens(tens) + " " + self.process_single(remainder) if remainder else self.process_tens(tens)
    
    def process_tens(self, num):
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

    def process_single(self, num):
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
    
    def process_sub_20(self, num):
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
