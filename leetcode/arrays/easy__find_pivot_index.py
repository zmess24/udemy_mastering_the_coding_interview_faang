# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        n = len(nums)
        for i in range(n):
            if i == 0:
                total = sum(nums[i+1:n])
                print(total)
                if total == 0:
                    return 0
            elif i == len(nums) - 1:
                total = sum(nums[0:i])
                if total == 0:
                    return n-1
            else:
                leftSum = sum(nums[0:i])
                rightSum = sum(nums[i+1:len(nums)])
                if leftSum == rightSum:
                    return i

        return pivot