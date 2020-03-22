#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):

    SA = 0
    h = len(A)
    w = len(A[0])
    
    for row in A:
        SA += row[0]
        for i in range(w - 1):
            SA += abs(row[i] - row[i+1])
        SA += row[-1]

    for j in range(w):
        SA += A[0][j]
        for i in range(h - 1):
            SA += abs(A[i][j] - A[i+1][j])
        SA += A[-1][j]

    return SA + 2 * h * w



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

