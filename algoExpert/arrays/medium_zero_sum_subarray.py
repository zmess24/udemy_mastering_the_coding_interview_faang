def zeroSumSubarray(nums):
    # Create 
    sums = set([0])
    # totalSum = 0
    currentSum = 0
    # Iterate through nums array:
    for num in nums:
        # Add current number to currentSum
        currentSum += num
        # If currentSum is in sums set
        if currentSum in sums:
            return True
        # Else, add currentSum to sums set.
        sums.add(currentSum)
            
    return False
