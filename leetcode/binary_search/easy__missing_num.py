# https://leetcode.com/problems/missing-number/description/

# O(n) Time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        missingNum = 0

        for i in range(maxNum):
            if missingNum not in nums:
                return missingNum

            missingNum += 1


        return missingNum + 1