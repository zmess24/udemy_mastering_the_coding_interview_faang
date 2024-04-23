# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def isValid(s):
    if len(s) == 1:
        return "YES"
        
    hashTable = {}
    ansTable = {}
    
    for index, char in enumerate(s):
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    
    maxCount, minCount = 0, float('inf')
    
    for key in hashTable:
        count = hashTable[key]
        if count in ansTable:
            ansTable[count].append(key)
        else:
            ansTable[count] = [key]
    
        maxCount = max(count, maxCount)
        minCount = min(count, minCount)
    
    if len(ansTable) == 1:
        return "YES"
    if len(ansTable) == 2:
        if len(ansTable[maxCount]) == 1 and maxCount - 1 == minCount:
            return "YES"
        elif minCount == 1 and len(ansTable[minCount]) == 1:
            return "YES"
    
    return "NO"