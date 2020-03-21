#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):

    sorted_list=[]
    for i in grid:
        sorted_list.append(sorted(i))
    
    for i in range(len(sorted_list)-1, -1, -1):
        index=len(sorted_list)-1
        while index>0:
            if sorted_list[index][i]<sorted_list[index-1][i]:
                return 'NO'
            else:
                index-=1
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

