#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    
    array_sorted = sorted(arr)
    if array_sorted == arr: print('yes')
    diff_indices = []
    start = None
    end = None
    for i in range(len(arr)):
        j = len(arr) - 1 - i
        if i <= j:   
            if arr[i] != array_sorted[i]:
                if not start:
                    start = i
                diff_indices.append(i)
            
            if arr[j] != array_sorted[j]:
                if not end:
                    end = j
                diff_indices.append(j)       
        else:                  
            break
    
    if not end:
        end = diff_indices[-1]
    if start == None:
        start = diff_indices[-1]

    if len(diff_indices) == 2:
        print('yes')
        print('swap', start + 1, end + 1)
    
    else:
        arr1 = arr[start : end + 1]
        arr2 = array_sorted[start : end + 1]
        arr2.reverse()

        if arr1 == arr2:      
            print('yes')
            print('reverse', start + 1, end + 1)
        else:
            print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
