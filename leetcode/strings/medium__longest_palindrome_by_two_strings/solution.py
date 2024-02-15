from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashMap = defaultdict(int)
        count = 0

        for word in words:
            if hashMap[word] > 0:
                count += 4
                hashMap[word] -= 1
            else:
                hashMap[word[::-1]] += 1
        
        remainder = 2 if any(char[0] == char[1] and value > 0 for char, value in hashMap.items()) else 0
        return count + remainder