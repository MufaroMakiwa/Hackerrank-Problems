#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):

    for i in range(1, len(arr)):
        test=arr[i]
        check_list=arr[:i+1]
        for j in range(len(check_list)-2, -1, -1):
            if check_list[j]>=test and check_list[j-1]<=test:
                arr.insert(j, test)
                del arr[i+1]
                print(*arr)
                inserted=True
                break
            else:
                inserted=False
        
        if  not inserted:
            print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

