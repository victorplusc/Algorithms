#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    min_diff = float('inf')
    candidates = [None, None]
    arr.sort()
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            candidates = [arr[i], arr[i+1]]
            min_diff = diff
        elif diff == min_diff:
            candidates.append(arr[i])
            candidates.append(arr[i+1])
    return candidates
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
