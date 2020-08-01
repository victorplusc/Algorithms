#!/bin/python3

import math
import os
import random
import re
import sys

class MStack():
    def __init__(self):
        self.stack = []
        self.s_max = 0
    
    def get_max(self):
        return self.s_max

    def push(self, val):
        self.s_max = max(val, self.s_max)
        self.stack.append([val, self.s_max])

    def pop(self):
        self.stack.pop()
        if self.stack:
            self.s_max = self.stack[-1][1]
        else:
            self.s_max = 0
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    max_stack = MStack()
    
    for q_itr in range(n):
        s = str(input())
        print("OP:{}".format(s))
        if s == "2":
            max_stack.pop()
        elif s == "3":
            fptr.write(str(max_stack.get_max()) + '\n')
            
        else:
            val = int(s.split()[1])
            max_stack.push(val)
    
    fptr.close()
