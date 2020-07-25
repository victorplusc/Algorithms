#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""
def timeConversion(s):
    #
    # Write your code here.
    #
    hours = int(s.split(":")[0])
    if s.endswith("PM"):
        hours+=12
    if s.endswith("AM"):
        if hours == 12:
            hours = 0
    hours = str(hours) if hours > 9 else "0"+str(hours)
    mins_secs = ":".join(s.strip("AM").strip("PM").strip("AM").split(":")[1:])
    return hours+":"+mins_secs

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
