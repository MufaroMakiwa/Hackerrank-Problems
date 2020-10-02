#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    def orientations():
        b1 = [[8,1,6], [3,5,7], [4,9,2]]
        yield b1

        b2 = [[4,9,2], [3,5,7], [8,1,6]]
        yield b2

        b3 = []
        b4 = []

        for i in range(3):
            row1 = []
            row2 = []
            for j in range(3):
                row1.append(b1[j][i])
                row2.append(b2[j][i])
            b3.append(row1)
            b4.append(row2)

        yield b3
        yield b4

        b5 = [[6,1,8], [7,5,3], [2,9,4]]
        yield b5

        b6 = [[2,9,4], [7,5,3], [6,1,8]]

        b7 = []
        b8 = []

        for i in range(3):
            row1 = []
            row2 = []
            for j in range(3):
                row1.append(b5[j][i])
                row2.append(b6[j][i])
            b7.append(row1)
            b8.append(row2)

        yield b7
        yield b8

    diff = float('inf')
    for ori in orientations():
        so_far = 0
        for i in range(3):
            for j in range(3):
                so_far += abs(s[i][j] - ori[i][j])
        if so_far < diff:
            diff = so_far

    return diff



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
