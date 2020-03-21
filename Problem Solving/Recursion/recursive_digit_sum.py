#!/bin/python

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    if len(n)==1:
        if k==1:
            return n
        else:
            return superDigit(n*k, 1)
    else:
        return superDigit(str(sum(int(i) for i in n)), k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

