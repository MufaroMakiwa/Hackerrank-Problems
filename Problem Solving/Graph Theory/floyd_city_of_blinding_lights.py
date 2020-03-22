#!/bin/python3

import math
import os
import random
import re
import sys
import copy


def find_path(graph, shortest, start, end, nodes):

    graph = dict(graph)
    shortest_path = dict(shortest)
    for node in graph:
        shortest_path[node] = float('inf')
    shortest_path[start] = 0
    seen = set()
    while graph:
        minNode = None
        for node in graph:
            if not minNode:
                minNode = node
            elif shortest_path[node] < shortest_path[minNode]:
                minNode = node
        
        if minNode == end:
            break

        for child in graph[minNode]:
            if child not in seen:
                current_dist = shortest_path[child]
                parent_dist = graph[minNode][child]
                parent = shortest_path[minNode]
                if parent + parent_dist < current_dist:
                    shortest_path[child] = parent + parent_dist  
        seen.add(minNode)
        del graph[minNode]
    

    
    if shortest_path[end] != float('inf'):
        return shortest_path[end]
    else:
        return -1
    

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    graph = {}
    shortest = {}
    found = set()
    for _ in range(road_edges):
        start, end, weight = list(map(int, input().split()))
        graph.setdefault(start, {})
        shortest[start] = float('inf')
        graph[start][end] = weight
        found.add(start)

    not_found = set(range(1, road_nodes + 1)) - found
    for node in not_found:
        shortest[node] = float('inf')
        graph.setdefault(node, {})
    
    q = int(input())
    
    found = {}
    for q_itr in range(q):
        start, end = list(map(int, input().split()))
        if start in found and end in found[start]:
                print(found[start][end])
        else:
            distance = find_path(graph, shortest, start, end, road_nodes)
            found.setdefault(start, {})
            found[start][end] = distance
            print(found[start][end])

