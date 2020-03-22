#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):

    to_sort=arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i]>to_sort:
            arr[i+1]=arr[i]
            print(*arr)

            if i==0:
                arr[0]=to_sort
                print(*arr)
                break

        elif arr[0]<=to_sort:
            arr[i+1]=to_sort
            print(*arr)
            break 
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

