#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r, c, obstacles):

    cells = []

    cells.append(((r-i, c+i) for i in range(1, n) if all(1<=j<=n for j in (r-i, c+i))))
    cells.append(((r+i, c-i) for i in range(1, n) if all(1<=j<=n for j in (r+i, c-i))))
    cells.append(((r-i, c-i) for i in range(1, n) if all(1<=j<=n for j in (r-i, c-i))))
    cells.append(((r+i, c+i) for i in range(1, n) if all(1<=j<=n for j in (r+i, c+i))))
    cells.append(((r-i, c) for i in range(1, n) if 1 <= r-i <= n))
    cells.append(((r+i, c) for i in range(1, n) if 1 <= r+i <= n))
    cells.append(((r, c-i) for i in range(1, n) if 1 <= c-i <= n))
    cells.append(((r, c+i) for i in range(1, n) if 1 <= c+i <= n))

    count = 0

    for collection in cells:
        for cell in collection:
            if cell in obstacles:
                break
            else:
                count += 1

    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r = int(r_qC_q[0])

    c = int(r_qC_q[1])

    obstacles = set()

    for _ in range(k):
        obstacles.add(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r, c, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

