class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        # Find max number of candies
        for numCandies in candies:
            maxCandies = numCandies if numCandies > maxCandies else maxCandies

        result = map(lambda numCandies: numCandies + extraCandies >= maxCandies, candies)

        return result

        