# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            ans = guess(mid)
            
            if ans == 0:
                return mid
            elif ans == -1:
                right = mid - 1
            elif ans == 1:
                left = mid + 1