#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):

    graph = {}
    distances = {}
    seen = {s}
    for i, j in edges:
        distances.setdefault(i, -1)
        distances.setdefault(j, -1)
        graph.setdefault(i, set())
        graph.setdefault(j, set())
        graph[i].add(j)
        graph[j].add(i)
    if s in distances:
        distances[s] = 0
    

    agenda = [s]
    while agenda:
        parent = agenda.pop(0)
        if parent in graph:
            for i in graph[parent]:
                if i not in seen:
                    if distances[i] == -1:  
                        distances[i] = 6 + distances[parent]   
                    else:
                        distances[i] += 6 + distances[parent]
                    agenda.append(i)
                    seen.add(i)

    result = []
    for i in range(1, n+1):
        if i != s:
            if i in distances:
                result.append(distances[i])
            else:
                result.append(-1)
    return result

    

    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

