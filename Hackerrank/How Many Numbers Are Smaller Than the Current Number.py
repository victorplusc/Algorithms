#!/bin/python3

import math
import os
import random
import re
import sys

def res(n, s):
    orig = [int(v) for v in s.split()]

    hmap = {}
    for i, val in enumerate(sorted(orig)):
        if val not in hmap:
            hmap[val] = i

    output = [hmap[num] for num in orig]
    
    return " ".join([str(v) for v in output])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    # for q_itr in range(q):
    s = str(input())

    result = res(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
