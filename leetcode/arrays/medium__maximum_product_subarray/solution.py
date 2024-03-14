class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Get the max of the provided numbers
        res = max(nums)
        # Set max & min = 1 
        currMin = 1
        currMax = 1
        # Begin Iteration
        for n in nums:
            # Store temp max in variable to prevent overwrite
            temp_max = n * currMax
            # Get current max between current * currentMax, n * currentMin, and n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp_max, n * currMin, n)
            res = max(res, currMax)

        return res

