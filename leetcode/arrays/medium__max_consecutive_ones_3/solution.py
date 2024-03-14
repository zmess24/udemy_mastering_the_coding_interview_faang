class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Get length of list
        n = len(nums)
        # Initialize Sliding Window Variables (left, right, countOfOnes, maxCount)
        left = 0
        right = 0
        countOfOnes = 0
        maxCount = 0

        # Start Iteration
        while right < n:
            # if currentIndex == 1:
            if nums[right] == 1:
                # increment countOfOnes by '1'
                countOfOnes += 1

            # If currentWindowLength - countOfOnes > k:
            if (right - left + 1) - countOfOnes > k:
                # If leftInfed == 1:
                if nums[left] == 1:
                    # Decrement countOfOnes by 1
                    countOfOnes -= 1
                # Increment left by 1
                
                left += 1
            
            right += 1
            # Assign maxCount to greater of maxCount and currentWindowLength
            maxCount = max(maxCount, right - left)

        # Return maxCount
        return maxCount



