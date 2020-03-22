#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the shortestReach function below.
def shortestReach(graph, s):

    shortest = {}
    for node in graph:
        shortest[node] = float('inf')
    shortest[s] = 0
    seen = set()
    while graph:
        minNode = None
        for node in graph:
            if minNode is None:
                minNode = node
            elif shortest[node] < shortest[minNode]:
                minNode = node

        for child in graph[minNode]:
            if child not in seen:
                dist = graph[minNode][child]
                parent = shortest[minNode]
                if dist + parent < shortest[child]:
                    shortest[child] = dist + parent
        seen.add(minNode)
        del graph[minNode]
    
    to_return = []
    for node in sorted(shortest.keys()):
        if node != s:
            if shortest[node] != float('inf'):
                to_return.append(shortest[node])
            else:
                to_return.append(-1)

    return to_return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        graph = {}
        present = set()
        for _ in range(m):
            i, j , k = list(map(int, input().rstrip().split()))
            present.update([i, j])
            graph.setdefault(i, {})
            graph.setdefault(j, {})
            if j in graph[i]:
                if k < graph[i][j]:
                    graph[i][j] = k
            else:
                graph[i][j] = k
            
            if i in graph[j]:
                if k < graph[j][i]:
                    graph[j][i] = k
            else:
                graph[j][i] = k
        
        not_present = set(range(1, n+1)) - present
        for node in not_present:
            graph.setdefault(node, {})

        s = int(input())

        result = shortestReach(graph, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

