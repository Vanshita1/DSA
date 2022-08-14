#!/bin/python3

import math
import os
import random
import re
#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.



import sys
from array import *

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minumum = arr[:4]
    minsum = sum(minumum)
    maximum = arr[1:]
    maxsum = sum(maximum)
    ans = str(minsum) + " " + str(maxsum)
    print(ans)
    
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    miniMaxSum(arr)
