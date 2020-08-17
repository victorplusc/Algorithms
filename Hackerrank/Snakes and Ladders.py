#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
import collections
def quickestWayUp(ladders, snakes):
    """
    The quickestWayUp function ishould return an integer that represents the minimum number of moves required.
    ladders: a 2D integer array where each contains the start and end cell numbers of a ladder
    snakes: a 2D integer array where each contains the start and end cell numbers of a snake
    """
    ladders = {ladders[i][0]: ladders[i][1] for i in range(len(ladders))}
    snakes = {snakes[i][0]: snakes[i][1] for i in range(len(snakes))}
    q = collections.deque([[0, 0]])
    visited = set()
    
    while q:
        loc, depth = q.popleft()
        visited.add(loc)
        if loc == 100:
            return depth
        for i in range(1, 7):
            if loc+i in visited: continue
            if loc+i in ladders:
                q.append([ladders[loc+i], depth+1])
            elif loc+i in snakes:
                q.append([snakes[loc+i], depth+1])
            else:
                q.append([loc+i, depth+1])

    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
