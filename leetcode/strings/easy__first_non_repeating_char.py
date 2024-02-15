from collections import Counter

def firstNonRepeatingCharacter(string):
    counts = Counter(string)

    for i in range(len(string)):
        if counts[string[i]] == 1:
            return i
    
    return -1
