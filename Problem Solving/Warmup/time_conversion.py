#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #


    if s[8:]=='AM':
        
        if s[:2]!='12':
            return s[:8]
        else:
            return '00'+s[2:8]

    elif s[:2]=='12':

        return s[:8]
        
    else:
        new=str(int(s[:2])+12)
       
        return new+s[2:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

