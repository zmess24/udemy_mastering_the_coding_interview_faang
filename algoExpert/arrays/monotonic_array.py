# https://www.algoexpert.io/questions/monotonic-array
# Zac Solution
def isMonotonic(array):
    # Edge Cases
    if array == [] or len(array) == 1: return True
    increasing = None
    start = 0
    # Establish Direction
    for i in range(1, len(array)):
        if array[i-1] != array[i]:
            increasing = array[i-1] < array[i]
            start = i + 1
            break

    # Start Iteration
    for i in range(start, len(array)):
        if increasing:
            if array[i-1] > array[i]:
                return False
        else:
            if array[i-1] < array[i]:
                return False
        

    return True

# AlgoExpert Solution
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            isNonDecreasing = False
        if array[i-1] > array[i]:
            isNonIncreasing = False
            
    return isNonDecreasing or isNonIncreasing
