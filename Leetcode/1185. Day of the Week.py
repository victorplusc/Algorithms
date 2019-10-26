"""
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:
The given dates are valid dates between the years 1971 and 2100.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n = (year-1971)*365 + sum(1 for i in range(1971, year) if i%4 == 0)
        
        if year%4 == 0:
            months[1] += 1
        for i in range(month-1):
            n += months[i]
        n += day - 1
        return week[(n+5)%7]
