#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    alpha = {chr(ord("a")+i):i for i in range(26)}
    n = len(s)//2
    ops = 0
    for i in range(n):
        if s[i] < s[-1-i]:
            ops += alpha[s[-1-i]] - alpha[s[i]]
        elif s[-1-i] < s[i]:
            ops += alpha[s[i]] - alpha[s[-1-i]]
    return ops
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
