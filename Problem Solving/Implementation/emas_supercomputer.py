 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.

def twoPluses(grid):

    def tile(length, pos):
        r, c = pos
        points = set()
        for i in range(-(length//2), length//2 + 1):
            points.add((r, c + i))
            points.add((r + i, c))      
        return points


    r, c = len(grid), len(grid[0])
    good = set()
    bad = set()
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'G':
                good.add((i, j))
            else:
                bad.add((i, j))
    

    def solve(good, bad, prod = 1, tiles = 0):

        if tiles == 2:
            yield prod
            
        else:
            for cell in ((i, j) for i in range(r) for j in range(c)):
                initial_good = set(good)
                initial_bad = set(bad)

                for i in range(1, min(r, c)+1, 2):
                    tile1 = tile(i, cell)
                    if tile1 <= good:
                        bad |= tile1
                        good -= tile1
                        new_prod = prod * len(tile1)

                        for other in solve(good, bad, new_prod, tiles + 1):
                            yield other
                        
                        good = set(initial_good)
                        bad = set(initial_bad)
                    else:
                        break

    return max(product for product in solve(good, bad))

                





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
