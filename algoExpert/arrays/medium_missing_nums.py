def missingNumbers(nums):
    # Define "n" (lnngth of nums + 2)
    n = len(nums) + 2
    # Define ans list
    ans = []
    # Iterate from 1 to n + 1:
    for i in range(1, n +1):
        # If current index is not in nums list,
        if i not in nums:
            # Append to answers list
            ans.append(i)
    # Return ans
    return ans
