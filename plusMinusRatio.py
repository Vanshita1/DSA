#!/bin/python3
#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_count = 0
    neg_count = 0
    zero_count = 0
    n = len(arr)
    for i in range(0,n):
        if arr[i] == 0:
            zero_count += 1
        elif arr[i] > 0:
            pos_count += 1
        else:
            neg_count += 1
    o1 = pos_count/n
    o2 = neg_count/n
    o3 = zero_count/n
    print(o1)
    print(o2)
    print(o3)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
