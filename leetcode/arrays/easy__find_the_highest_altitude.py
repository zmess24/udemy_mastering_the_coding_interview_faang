# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0] * n
        prefix[0] = 0 + gain[0]

        for i in range(1, len(gain)):
            prefix[i] = prefix[i-1] + gain[i]

        return 0 if max(prefix) < 0 else max(prefix)