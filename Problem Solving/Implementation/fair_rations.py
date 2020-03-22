#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    
    if sum(B) % 2:
        return 'NO'
    
    count = 0
    index = 0
    while index < len(B):
        if B[index] % 2:
            B[index] += 1
            B[index + 1] += 1
            count += 2
        index += 1
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
