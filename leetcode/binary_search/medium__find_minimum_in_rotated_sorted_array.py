class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            # Break Case
            if nums[mid - 1] < nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            # If the left pointer is less than the mind pointer, pivot is to right
            elif nums[left] < nums[mid]:
                left = mid
            # else, pivot is to left
            else:
                right = mid

        return nums[0] 