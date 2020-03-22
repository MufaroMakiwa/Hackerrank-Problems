#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    g_r = len(G)
    g_c = len(G[0])
    p_r = len(P)
    p_c = len(P[0])

    for i in range(g_r - p_r + 1):
        for j in range(g_c - p_c + 1):
            sub = G[i][j:]
            if P[0] in sub and sub.index(P[0]) == 0:
                index = i + 1
                for k in range(1, p_r):
                    smaller = G[index][j:]
                    if P[k] in smaller and smaller.index(P[k]) == 0:
                        index += 1
                    else:
                        break
                else:
                    return 'YES'
            else:
                continue
    return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
