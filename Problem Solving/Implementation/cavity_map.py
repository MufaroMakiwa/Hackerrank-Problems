#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.


def cavityMap(grid):

    r = len(grid)
    output = []
    
    for i in range(r):
        if i == 0 or i == r - 1:
            output.append(grid[i])
        else:
            sub_string = ''
            for j in range(r):
                if j == 0 or j == r-1:
                    sub_string += grid[i][j]
                else:
                    neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                    depth = grid[i][j]
                    for pos in neighbours:
                        row, col = pos
                        if grid[row][col] >= depth:
                            sub_string += depth
                            break
                    else:
                        sub_string += 'X'
            output.append(sub_string)
    
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
