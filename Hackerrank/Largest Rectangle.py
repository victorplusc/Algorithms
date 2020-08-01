#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(height):
    width = len(height)
    largest = float('-inf')
    for i in range(width):
        for j in range(i, width):
            min_height = float('inf')
            for k in range(i, j+1):
                min_height = min(min_height, height[k])
            largest = max(largest, min_height*(j-i+1))
    return largest
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
