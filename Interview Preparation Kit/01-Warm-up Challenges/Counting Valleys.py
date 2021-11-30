#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    count=0
    res=0
    for c in path:
        if c=='U':
            count+=1
        else: 
            count-=1  
        if count==0 and c=='U':
            res+=1           
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
