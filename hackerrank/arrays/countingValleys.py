#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(steps, path):
    state = { "U": 1, "D" : -1 }
    valleys = 0
    currentElevation = 0
    for step in path:
        direction = state[step]
        if currentElevation == -1 and direction == 1:
            valleys += 1
    
        currentElevation = currentElevation + state[step]
    
    return valleys
