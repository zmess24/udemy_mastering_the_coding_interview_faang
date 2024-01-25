class Solution:
    def longestPalindrome(self, s: str) -> int:
        lettersMap = {}
        longest = 0

        for char in s:
            if char in lettersMap:
                lettersMap.pop(char)
                longest += 2
            else:
                lettersMap[char] = 1
        
        if lettersMap:
            longest += 1

        return longest