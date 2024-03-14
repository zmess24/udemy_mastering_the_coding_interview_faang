import math
import numpy as np

def solution(a, k):
    lowSize = 0
    maxSize = max(a)
    
    while lowSize < maxSize:
        mid = (lowSize + maxSize + 1) >> 1
        ribbonCount = 0
        
        for ribbon in a:
            ribbonCount += ribbon // mid
        
        print(lowSize, mid, maxSize, ribbonCount)
        
        if ribbonCount < k:
            maxSize = mid - 1
        else:
            lowSize = mid
            
    return lowSize