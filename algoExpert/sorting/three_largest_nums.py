def findThreeLargestNumbers(array):
    # Initialze answer array with first three numbers in input array (0, 1, 2)
    ans = []
    for i in range(3): 
        ans.append(array[i])
        
    # Iterate over input array starting at 3rd index (3)
    for i in range(3, len(array)):
        # Check if current number is bigger than the min of the answer array
        currentMin = min(ans)
        if array[i] > currentMin:
            # If it is, replace the minimums numbers index in the answer array with the current number 
            index = ans.index(currentMin)
            ans[index] = array[i]
            
    # return sorted array
    return sorted(ans)
