# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashMap = Counter(nums)
        matches = set()

        if k == 0:
            count = sum(1 for freq in hashMap.values() if freq>1)
            return count

        for num in nums:
            numToFind = num + k
            if numToFind in hashMap and (num, numToFind) not in matches:
                matches.add((num,numToFind))

        return len(matches)

