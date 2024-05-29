# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Base Cases
        if n == 0: return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and (n == 0 or n == 1): return True
        # Keep Track of Flowers
        flowersLeft = n

        for i, flower in enumerate(flowerbed):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    flowersLeft -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    flowersLeft -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    flowersLeft -= 1
            
            if flowersLeft == 0: return True
        
        return False