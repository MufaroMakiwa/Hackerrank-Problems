#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):

    values=list('0'*100)
    for i in arr:
        values[i]=int(values[i])+1

    results=[]
    for i in range(100):
        for j in range(int(values[i])):
            results.append(i)

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join((map(str, result))))
    fptr.write('\n')

    fptr.close()

