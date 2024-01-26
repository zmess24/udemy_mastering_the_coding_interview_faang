class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create dictionary of numbers, with the numbers as the key and indicie as the value
        numberDict = {}
        # Iterate over 'nums' list:
        for i in range(len(nums)):
            # If current value exists in dictionary:
            if nums[i] in numberDict:
                # return index in dictionary and current index inside a list
                return [numberDict[nums[i]], i]
            # If current value doesn't exist in dictionary:
            else:
                # Get the difference betwen the target & current value
                difference = target - nums[i]
                # Add difference as key to dictionary with current index as value
                numberDict[difference] = i
        # return false if not matches found
        return False





