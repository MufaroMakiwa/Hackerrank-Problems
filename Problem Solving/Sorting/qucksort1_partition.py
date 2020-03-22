#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):

    left=[]
    right=[]
    equal=[]
    for i in arr:
        if i<arr[0]:
            left.append(i)
        elif i>arr[0]:
            right.append(i)
        else:
            equal.append(i)

    return left+equal+right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


