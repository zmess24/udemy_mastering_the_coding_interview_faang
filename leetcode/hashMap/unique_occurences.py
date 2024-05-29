# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        # Iterate through each element in array to get counts
        for element in arr:
            if element in hashMap:
                hashMap[element] += 1
            else:
                hashMap[element] = 1

        counts = set([])
        for count in hashMap.values():
            if count in counts: return False
            else: counts.add(count)

        return True


    