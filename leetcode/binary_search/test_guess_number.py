# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# BS
class Solution:
    def guessNumber(self, n: int) -> int:
        # left = 0, right = n
        left, right = 0, n
        # while left != right:
        while left <= right:
            # Get mid-point of n assigned to "mid"
            mid = (left + right) // 2
            # Call guess API
            ans = guess(mid)
            # If ans == -1 (mid is higher than target):
            if ans == -1:
                # right = mid - 1
                right = mid - 1
            # If ans == 1 (mid is lower than target):
            if ans == 1:
                # left = mid + 1
                left = mid + 1
            # if ans == 0 (mid is target)
            if ans == 0:
                # return mid
                return mid