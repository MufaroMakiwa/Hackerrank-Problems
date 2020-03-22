#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**8)

# Complete the journeyToMoon function below.
def journeyToMoon(graph, n):

    used = set()
    def make_country(graph,  node): 
        used.add(node) 
        to_return = []
        children = set(graph[node]) - used
        if children:      
            for child in children:
                for other in make_country(graph, child):
                    to_return.append(other)
        to_return.append(node)
        return to_return

    seen = set()
    countries = []
    for node in graph:
        if node not in seen:
            country = set(make_country(graph, node))
            countries.append(country)
            seen.update(country)

    pairs = 0
    done = 0
    for i in range(len(countries) - 1):
        done += len(countries[i])
        not_in = n - done
        pairs += not_in * len(countries[i])

    return pairs
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, p = list(map(int, input().split()))
    graph = {}
    seen = set()
    for _ in range(p):
        a, b = list(map(int, input().rstrip().split()))
        graph.setdefault(a, set())
        graph[a].add(b)
        graph.setdefault(b, set())
        graph[b].add(a)
        seen.update([a, b])
    
    not_found = set(range(n)) - seen
    for i in not_found:
        graph.setdefault(i, set())
        

    result = journeyToMoon(graph, n)

    fptr.write(str(result) + '\n')

    fptr.close()

