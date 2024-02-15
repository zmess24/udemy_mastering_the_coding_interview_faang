from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        
        hashMap = Counter(s)
        oddCount = 0

        for char in hashMap:
            if hashMap[char] % 2 == 1:
                oddCount +=1 

        return False if oddCount > k else True
        
        