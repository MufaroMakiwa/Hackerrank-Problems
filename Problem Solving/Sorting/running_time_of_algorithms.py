#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(l):
    moves=0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]

        while (j >= 0) and (l[j] > key):
           l[j+1], l[j] = l[j], key 
           moves+=1      
           j -= 1
    return moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

