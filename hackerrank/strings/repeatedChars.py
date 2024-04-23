#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    length, count = len(s), 0
    for char in s:
        if char == 'a':
            count += 1
    
    ans = count * math.floor(n / length)
    
    if n % length == 0:
        return ans
    else:
        for i in range(0, n % length):
            if s[i] == 'a':
                ans += 1
    
    return ans