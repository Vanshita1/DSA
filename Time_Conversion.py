#!/bin/python3
#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    times = re.search(r"(?P<hh>..):(?P<mm>..):(?P<ss>..)(?P<ampm>..)", s)
    hour = times.group('hh')
    if times.group('ampm') == 'PM':
        if hour == '12':
            hr = '12'
        else:
            hr = str(int(hour) + 12)
    else:
        if hour == '12':
            hr = '00'
        else:
            hr = hour
    return hr + ':' + times.group('mm') + ':' + times.group('ss')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
