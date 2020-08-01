#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
import collections
def anagram(s):
    if len(s)%2 != 0: 
        return -1
    n = len(s)//2
    s1 = s[:n]
    s2 = s[n:]

    count1 = collections.Counter(s1)
    count2 = collections.Counter(s2)
    
    to_change = 0
    for c in count1:
        if count2[c] < count1[c]:
            to_change += count1[c] - count2[c]

    return to_change

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
